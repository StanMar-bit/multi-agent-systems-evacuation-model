"""Analysis of the BehaviorSpace experiments (experiment-1, experiment-2, sensitivity).

Usage:  python3 analysis/analyze.py results/
Reads   results/experiment-1.csv, results/experiment-2.csv, results/sensitivity.csv
        (BehaviorSpace "table" output of main.nlogox)
Writes  analysis/figures/*.png and analysis/summary.md

Statistics
- Every condition ran with fire-seed 1-10, so every condition faced the same 10
  fires. The fire is therefore a blocking factor: it is added to every model
  (C(fire)) so that differences between fires do not hide the effects.
- Experiment 1: three-way ANOVA (helpers x alarm x trained, all interactions)
  plus the fire block, type II sums of squares, partial eta squared.
- Experiment 2: one-way ANOVA (strategy) plus the fire block, Tukey HSD.
- Evacuation times are skewed and casualties are counts, so every ANOVA is
  checked with a non-parametric test (Kruskal-Wallis) on the same factor.
- Sensitivity: each variant is compared with the baseline on the same fires
  (paired Wilcoxon signed-rank test).
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
from scipy import stats
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

RESULTS = Path(sys.argv[1] if len(sys.argv) > 1 else "results")
OUT = Path(__file__).parent
FIG = OUT / "figures"
FIG.mkdir(parents=True, exist_ok=True)

# BehaviorSpace column names -> short names
RENAME = {
    "[run number]": "run",
    "fire-seed": "fire",
    "number-of-helpers": "helpers",
    "alarm-type": "alarm",
    "proportion-trained": "trained",
    "cognitive-strategy": "strategy",
    "panic-threshold": "panic_threshold",
    "vision-radius": "vision_radius",
    "companion-probability": "companion_probability",
    "number-of-evacuees": "evacuees",
    "total-evacuation-time": "evac_time",
    "time-until-out 0.5": "t50",
    "time-until-out 0.9": "t90",
    "casualties": "casualties",
    'count-in-state "incapacitated"': "incapacitated",
    "evacuated-count": "evacuated",
    "count evacuees": "left_inside",
    "mean-reaction-time": "reaction_time",
    'share-of-time-in "rational"': "share_rational",
    'share-of-time-in "familiar"': "share_familiar",
    'share-of-time-in "follower"': "share_follower",
    'share-of-time-in "panic"': "share_panic",
    "detection-delay": "alarm_time",
    "length flashed-over-rooms": "rooms_flashed",
}
LABELS = {
    "evac_time": "Total evacuation time (s)",
    "t50": "Time until 50% out (s)",
    "t90": "Time until 90% out (s)",
    "casualties": "Casualties",
    "reaction_time": "Mean reaction time (s)",
}
ALARMS = ["none", "slow whoop", "voice"]
STRATEGIES = ["all rational", "all familiar", "all follower", "all panic", "arousal-based"]
STATES = ["rational", "familiar", "follower", "panic"]
STATE_COLORS = {"rational": "#2e7d32", "familiar": "#1565c0", "follower": "#ef6c00", "panic": "#c62828"}

sns.set_theme(style="whitegrid", context="paper", font_scale=1.1)
summary = ["# Results of the BehaviorSpace experiments", ""]


def load(name):
    df = pd.read_csv(RESULTS / f"{name}.csv", skiprows=6)
    df = df.rename(columns=RENAME)
    # t50 / t90 are -1 when that share never got out before the end of the run:
    # censor them at the run length (max-duration, 900 s), so the slowest runs
    # are not dropped from the analysis
    limit = df["max-duration"] if "max-duration" in df else 900
    for col in ["t50", "t90"]:
        if col in df:
            df[f"{col}_censored"] = df[col] < 0
            df[col] = df[col].where(df[col] >= 0, limit)
    return df


def add(text=""):
    summary.append(text)


def describe(df, by, cols):
    """Median [IQR] and mean (SD) per group, as a markdown table."""
    rows = []
    for key, g in df.groupby(by, sort=False):
        row = {by if isinstance(by, str) else " x ".join(by): key}
        for c in cols:
            v = g[c].dropna()
            row[c] = f"{v.median():.0f} [{v.quantile(.25):.0f}-{v.quantile(.75):.0f}]; {v.mean():.1f} ({v.std():.1f})"
        rows.append(row)
    return pd.DataFrame(rows).to_markdown(index=False)


def anova_table(model):
    table = anova_lm(model, typ=2)
    resid = table.loc["Residual", "sum_sq"]
    table["partial_eta2"] = table["sum_sq"] / (table["sum_sq"] + resid)
    table.loc["Residual", "partial_eta2"] = np.nan
    return table


def fmt_anova(table):
    out = table[["df", "F", "PR(>F)", "partial_eta2"]].copy()
    out.columns = ["df", "F", "p", "partial eta2"]
    return out.round({"df": 0, "F": 2, "p": 4, "partial eta2": 3}).to_markdown()


# ---------------------------------------------------------------------------
# Experiment 1: helpers x alarm x trained
# ---------------------------------------------------------------------------
e1 = load("experiment-1")
e1["alarm"] = pd.Categorical(e1["alarm"], ALARMS, ordered=True)
add("## Experiment 1: helpers x alarm type x proportion trained")
add(f"{len(e1)} runs ({e1.groupby(['helpers', 'alarm', 'trained'], observed=True).ngroups} conditions x "
    f"{e1['fire'].nunique()} fires). Runs that ended with people still inside: {(e1['left_inside'] > 0).sum()}; "
    f"t90 censored at 900 s: {e1['t90_censored'].sum()}.")
add()
for dv in ["t90", "evac_time", "reaction_time", "casualties"]:
    model = smf.ols(f"{dv} ~ C(helpers) * C(alarm) * C(trained) + C(fire)", data=e1).fit()
    add(f"### {LABELS[dv]}: three-way ANOVA with the fire as block (type II)")
    add(fmt_anova(anova_table(model)))
    add()
    for factor in ["helpers", "alarm", "trained"]:
        groups = [g[dv].dropna() for _, g in e1.groupby(factor, observed=True)]
        h, p = stats.kruskal(*groups)
        add(f"- Kruskal-Wallis {dv} by {factor}: H = {h:.2f}, p = {p:.4g}")
    add()
add("### Descriptives per factor: median [IQR]; mean (SD)")
for factor in ["alarm", "trained", "helpers"]:
    add(describe(e1.sort_values(factor), factor, ["t90", "evac_time", "reaction_time", "casualties", "incapacitated"]))
    add()

# share of cognitive states vs evacuation time (proposal: relate shares to evacuation time)
e1["share_aroused"] = e1["share_follower"] + e1["share_panic"]
rho, p = stats.spearmanr(e1["share_aroused"], e1["t90"], nan_policy="omit")
rho_p, p_p = stats.spearmanr(e1["share_panic"], e1["casualties"])
add(f"- Spearman: share of time follower+panic vs time until 90% out: rho = {rho:.2f}, p = {p:.4g}")
add(f"- Spearman: share of time in panic vs casualties: rho = {rho_p:.2f}, p = {p_p:.4g}")
add()

# Figure 1: time until 90% out per condition
g = sns.catplot(data=e1, x="alarm", y="t90", hue="trained", col="helpers", col_wrap=2, kind="box",
                palette="Blues", height=2.3, aspect=1.15, legend_out=True, fliersize=2, linewidth=0.8)
g.set_axis_labels("Alarm type", LABELS["t90"])
g.set_titles("{col_name} helpers")
g._legend.set_title("Proportion\ntrained")
g.savefig(FIG / "exp1_t90.png", dpi=200)
plt.close("all")

# Figure 2: reaction time and casualties by alarm type
fig, axes = plt.subplots(1, 2, figsize=(8, 3.2))
sns.boxplot(data=e1, x="alarm", y="reaction_time", hue="trained", palette="Blues", ax=axes[0])
axes[0].set(xlabel="Alarm type", ylabel=LABELS["reaction_time"])
axes[0].legend(title="Trained", fontsize=8)
sns.boxplot(data=e1, x="helpers", y="casualties", hue="trained", palette="Blues", ax=axes[1])
axes[1].set(xlabel="Number of helpers", ylabel=LABELS["casualties"])
axes[1].legend(title="Trained", fontsize=8)
fig.tight_layout()
fig.savefig(FIG / "exp1_reaction_casualties.png", dpi=200)
plt.close(fig)

# Figure 3: share of time in each cognitive state per condition
shares = (e1.groupby(["helpers", "alarm", "trained"], observed=True)
          [[f"share_{s}" for s in STATES]].mean().reset_index())
fig, axes = plt.subplots(2, 2, figsize=(6.0, 4.6), sharey=True)
axes = axes.flatten()
for ax, (h, sub) in zip(axes, shares.groupby("helpers")):
    labels = [f"{ {'none': 'N', 'slow whoop': 'W', 'voice': 'V'}[a] }\n{t:g}" for a, t in zip(sub["alarm"], sub["trained"])]
    bottom = np.zeros(len(sub))
    for s in STATES:
        ax.bar(labels, sub[f"share_{s}"], bottom=bottom, color=STATE_COLORS[s], label=s)
        bottom += sub[f"share_{s}"].to_numpy()
    ax.set_title(f"{h} helpers")
    ax.tick_params(axis="x", labelsize=7)
axes[0].set_ylabel("Share of moving time")
axes[2].set_ylabel("Share of moving time")
axes[1].legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize=8)
fig.supxlabel("Alarm (N = none, W = slow whoop, V = voice) / proportion trained", fontsize=9)
fig.tight_layout()
fig.savefig(FIG / "exp1_states.png", dpi=200)
plt.close(fig)

# ---------------------------------------------------------------------------
# Experiment 2: forced cognitive strategies
# ---------------------------------------------------------------------------
e2 = load("experiment-2")
e2["strategy"] = pd.Categorical(e2["strategy"], STRATEGIES, ordered=True)
add("## Experiment 2: forced cognitive strategies (slow whoop, no helpers)")
add(f"{len(e2)} runs. Runs that ended with people still inside: {(e2['left_inside'] > 0).sum()}; "
    f"runs where 90% never got out (t90 censored at 900 s): {e2['t90_censored'].sum()} "
    f"({', '.join(f'{k}: {v}' for k, v in e2.groupby('strategy', observed=True)['t90_censored'].sum().items() if v)}).")
add()
add(describe(e2.sort_values("strategy"), "strategy", ["t90", "evac_time", "casualties", "incapacitated", "left_inside"]))
add()
for dv in ["t90", "evac_time", "casualties"]:
    model = smf.ols(f"{dv} ~ C(strategy) + C(fire)", data=e2).fit()
    add(f"### {LABELS[dv]}: one-way ANOVA with the fire as block")
    add(fmt_anova(anova_table(model)))
    groups = [g[dv].dropna() for _, g in e2.groupby("strategy", observed=True)]
    h, p = stats.kruskal(*groups)
    add(f"\nKruskal-Wallis: H = {h:.2f}, p = {p:.4g}")
    data = e2.dropna(subset=[dv])
    tukey = pairwise_tukeyhsd(data[dv], data["strategy"].astype(str))
    add("\nTukey HSD:\n\n```\n" + str(tukey.summary()) + "\n```\n")

fig, axes = plt.subplots(1, 2, figsize=(8, 3.4))
order = STRATEGIES
pal = ["#2e7d32", "#1565c0", "#ef6c00", "#c62828", "#757575"]
sns.boxplot(data=e2, x="strategy", y="evac_time", hue="strategy", order=order, palette=pal, legend=False, ax=axes[0])
axes[0].set(xlabel="", ylabel=LABELS["evac_time"])
sns.boxplot(data=e2, x="strategy", y="casualties", hue="strategy", order=order, palette=pal, legend=False, ax=axes[1])
axes[1].set(xlabel="", ylabel=LABELS["casualties"])
for ax in axes:
    ax.tick_params(axis="x", rotation=35, labelsize=8)
fig.tight_layout()
fig.savefig(FIG / "exp2_strategies.png", dpi=200)
plt.close(fig)

# ---------------------------------------------------------------------------
# Sensitivity analysis
# ---------------------------------------------------------------------------
sens = load("sensitivity")
base = {"panic_threshold": 0.75, "vision_radius": 10, "companion_probability": 0.3, "evacuees": 150}
def variant(row):
    for k, v in base.items():
        if not np.isclose(row[k], v):
            return f"{k} = {row[k]:g}"
    return "baseline"
sens["variant"] = sens.apply(variant, axis=1)
add("## Sensitivity analysis (one parameter at a time; slow whoop, no helpers, 50% trained)")
add()
baseline = sens[sens["variant"] == "baseline"].set_index("fire")
rows = []
for name, g in sens.groupby("variant"):
    g = g.set_index("fire")
    row = {"variant": name}
    for dv in ["t90", "casualties", "share_panic"]:
        row[dv] = f"{g[dv].mean():.2f}"
        if name != "baseline":
            diff = (g[dv] - baseline[dv]).dropna()
            p = stats.wilcoxon(diff).pvalue if (diff != 0).any() else 1.0
            row[f"{dv} vs baseline p"] = f"{p:.3f}"
    rows.append(row)
add(pd.DataFrame(rows).to_markdown(index=False))
add()

fig, axes = plt.subplots(1, 2, figsize=(9, 3.6))
order = ["baseline"] + sorted(v for v in sens["variant"].unique() if v != "baseline")
for ax, dv in zip(axes, ["t90", "casualties"]):
    sns.pointplot(data=sens, y="variant", x=dv, order=order, errorbar=("ci", 95), linestyle="none", ax=ax, color="#1565c0")
    ax.axvline(baseline[dv].mean(), color="grey", ls="--", lw=1)
    ax.set(xlabel=LABELS[dv], ylabel="")
fig.tight_layout()
fig.savefig(FIG / "sensitivity.png", dpi=200)
plt.close(fig)

# ---------------------------------------------------------------------------
# Illustrations of one run (optional files: results/timeseries.csv, results/view-*.png)
# north-west office fire, fire-seed 3, slow whoop, 50% trained, 150 evacuees
# ---------------------------------------------------------------------------
ts_file = RESULTS / "timeseries.csv"
if ts_file.exists():
    ts = pd.read_csv(ts_file, skiprows=6)
    ts = ts.rename(columns={"[step]": "t"})
    names = ["unaware", "waiting", "rational", "familiar", "follower", "panic"]
    colors = ["#575757", "#92921d"] + [STATE_COLORS[s] for s in STATES]
    if 'count-in-state "incapacitated"' in ts:
        names.append("incapacitated")
        colors.append("#000000")
    cols = [f'count-in-state "{n}"' for n in names]
    fig, ax = plt.subplots(figsize=(4.6, 2.8))
    ax.stackplot(ts["t"], *[ts[c] for c in cols], labels=names, colors=colors, alpha=0.9)
    ax.plot(ts["t"], ts["evacuated-count"], color="black", lw=1.2, label="evacuated")
    alarm = ts["detection-delay"].max()
    if alarm >= 0:
        ax.axvline(alarm, color="black", ls=":", lw=1)
        ax.text(alarm + 5, ax.get_ylim()[1] * 0.92, "alarm", fontsize=7)
    flash = ts.loc[ts["length flashed-over-rooms"] > 0, "t"]
    if len(flash):
        ax.axvline(flash.min(), color="#c62828", ls=":", lw=1)
        ax.text(flash.min() + 5, ax.get_ylim()[1] * 0.80, "flashover", fontsize=7, color="#c62828")
    ax.set(xlabel="Time (s)", ylabel="Number of evacuees", xlim=(0, ts["t"].max()))
    ax.legend(fontsize=6.5, loc="center right", ncol=1)
    fig.tight_layout()
    fig.savefig(FIG / "run_timeseries.png", dpi=220)
    plt.close(fig)

views = [RESULTS / "view-120.png", RESULTS / "view-200.png"]
if all(v.exists() for v in views):
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.9))
    for ax, v, title in zip(axes, views, ["t = 120 s: smoke in the office, people walking out",
                                          "t = 200 s: office flashed over, smoke in the hall"]):
        ax.imshow(plt.imread(v))
        ax.set_title(title, fontsize=8)
        ax.axis("off")
    fig.tight_layout()
    fig.savefig(FIG / "run_views.png", dpi=220)
    plt.close(fig)

(OUT / "summary.md").write_text("\n".join(summary))
print("\n".join(summary))
