# Results of the BehaviorSpace experiments

## Experiment 1: helpers x alarm type x proportion trained
360 runs (36 conditions x 10 fires). Runs that ended with people still inside: 40; t90 censored at 900 s: 11.

### Time until 90% out (s): three-way ANOVA with the fire as block (type II)
|                                |   df |      F |        p |   partial eta2 |
|:-------------------------------|-----:|-------:|---------:|---------------:|
| C(helpers)                     |    3 |  53.95 |   0      |          0.339 |
| C(alarm)                       |    2 | 269.06 |   0      |          0.631 |
| C(trained)                     |    2 |   5.56 |   0.0042 |          0.034 |
| C(fire)                        |    9 |   6.84 |   0      |          0.164 |
| C(helpers):C(alarm)            |    6 |  23.55 |   0      |          0.31  |
| C(helpers):C(trained)          |    6 |   1.29 |   0.261  |          0.024 |
| C(alarm):C(trained)            |    4 |   1.5  |   0.2031 |          0.019 |
| C(helpers):C(alarm):C(trained) |   12 |   1.03 |   0.4202 |          0.038 |
| Residual                       |  315 | nan    | nan      |        nan     |

- Kruskal-Wallis t90 by helpers: H = 52.62, p = 2.204e-11
- Kruskal-Wallis t90 by alarm: H = 182.25, p = 2.663e-40
- Kruskal-Wallis t90 by trained: H = 2.82, p = 0.2445

### Total evacuation time (s): three-way ANOVA with the fire as block (type II)
|                                |   df |      F |        p |   partial eta2 |
|:-------------------------------|-----:|-------:|---------:|---------------:|
| C(helpers)                     |    3 |  72.57 |   0      |          0.409 |
| C(alarm)                       |    2 | 172.57 |   0      |          0.523 |
| C(trained)                     |    2 |   7.06 |   0.001  |          0.043 |
| C(fire)                        |    9 |   5.42 |   0      |          0.134 |
| C(helpers):C(alarm)            |    6 |  14.2  |   0      |          0.213 |
| C(helpers):C(trained)          |    6 |   0.31 |   0.9314 |          0.006 |
| C(alarm):C(trained)            |    4 |   1.27 |   0.2819 |          0.016 |
| C(helpers):C(alarm):C(trained) |   12 |   0.66 |   0.7857 |          0.025 |
| Residual                       |  315 | nan    | nan      |        nan     |

- Kruskal-Wallis evac_time by helpers: H = 79.56, p = 3.812e-17
- Kruskal-Wallis evac_time by alarm: H = 152.52, p = 7.596e-34
- Kruskal-Wallis evac_time by trained: H = 5.62, p = 0.06033

### Mean reaction time (s): three-way ANOVA with the fire as block (type II)
|                                |   df |      F |        p |   partial eta2 |
|:-------------------------------|-----:|-------:|---------:|---------------:|
| C(helpers)                     |    3 |  23.89 |   0      |          0.185 |
| C(alarm)                       |    2 | 180.11 |   0      |          0.533 |
| C(trained)                     |    2 |   0.34 |   0.7156 |          0.002 |
| C(fire)                        |    9 |   4.74 |   0      |          0.119 |
| C(helpers):C(alarm)            |    6 |   7.53 |   0      |          0.125 |
| C(helpers):C(trained)          |    6 |   0.92 |   0.4816 |          0.017 |
| C(alarm):C(trained)            |    4 |   0.28 |   0.8879 |          0.004 |
| C(helpers):C(alarm):C(trained) |   12 |   0.91 |   0.5333 |          0.034 |
| Residual                       |  315 | nan    | nan      |        nan     |

- Kruskal-Wallis reaction_time by helpers: H = 55.62, p = 5.061e-12
- Kruskal-Wallis reaction_time by alarm: H = 142.25, p = 1.29e-31
- Kruskal-Wallis reaction_time by trained: H = 0.50, p = 0.7803

### Casualties: three-way ANOVA with the fire as block (type II)
|                                |   df |      F |        p |   partial eta2 |
|:-------------------------------|-----:|-------:|---------:|---------------:|
| C(helpers)                     |    3 |   6.89 |   0.0002 |          0.062 |
| C(alarm)                       |    2 |   5.96 |   0.0029 |          0.036 |
| C(trained)                     |    2 |  13.76 |   0      |          0.08  |
| C(fire)                        |    9 |   4.68 |   0      |          0.118 |
| C(helpers):C(alarm)            |    6 |   1.37 |   0.2249 |          0.025 |
| C(helpers):C(trained)          |    6 |   3.31 |   0.0036 |          0.059 |
| C(alarm):C(trained)            |    4 |   2.26 |   0.0622 |          0.028 |
| C(helpers):C(alarm):C(trained) |   12 |   0.64 |   0.807  |          0.024 |
| Residual                       |  315 | nan    | nan      |        nan     |

- Kruskal-Wallis casualties by helpers: H = 19.28, p = 0.0002398
- Kruskal-Wallis casualties by alarm: H = 11.97, p = 0.002515
- Kruskal-Wallis casualties by trained: H = 32.27, p = 9.82e-08

### Descriptives per factor: median [IQR]; mean (SD)
| alarm      | t90                          | evac_time                    | reaction_time                | casualties         | incapacitated      |
|:-----------|:-----------------------------|:-----------------------------|:-----------------------------|:-------------------|:-------------------|
| none       | 420 [292-579]; 459.9 (201.1) | 511 [366-813]; 565.3 (232.4) | 229 [150-312]; 242.4 (117.3) | 0 [0-1]; 1.0 (3.0) | 0 [0-0]; 0.7 (2.7) |
| slow whoop | 236 [209-267]; 252.2 (90.2)  | 312 [268-379]; 375.8 (189.3) | 126 [101-142]; 122.5 (27.1)  | 0 [0-0]; 1.0 (2.8) | 0 [0-0]; 0.1 (0.4) |
| voice      | 208 [186-226]; 204.7 (29.9)  | 250 [225-287]; 264.0 (66.6)  | 110 [90-124]; 107.2 (25.1)   | 0 [0-0]; 0.2 (0.6) | 0 [0-0]; 0.0 (0.0) |

|   trained | t90                          | evac_time                    | reaction_time                | casualties         | incapacitated      |
|----------:|:-----------------------------|:-----------------------------|:-----------------------------|:-------------------|:-------------------|
|       0   | 242 [207-369]; 326.2 (198.2) | 324 [260-512]; 428.1 (233.9) | 127 [107-164]; 154.7 (86.7)  | 0 [0-1]; 1.5 (3.7) | 0 [0-0]; 0.7 (2.7) |
|       0.5 | 242 [210-329]; 303.2 (155.8) | 321 [269-468]; 409.2 (215.7) | 132 [104-171]; 156.5 (82.4)  | 0 [0-0]; 0.6 (1.7) | 0 [0-0]; 0.1 (0.4) |
|       1   | 232 [201-290]; 287.4 (149.3) | 286 [247-393]; 367.8 (194.7) | 124 [104-157]; 160.9 (109.0) | 0 [0-0]; 0.1 (0.4) | 0 [0-0]; 0.0 (0.2) |

|   helpers | t90                          | evac_time                    | reaction_time                | casualties         | incapacitated      |
|----------:|:-----------------------------|:-----------------------------|:-----------------------------|:-------------------|:-------------------|
|         0 | 269 [228-554]; 393.6 (225.7) | 461 [304-900]; 548.0 (269.9) | 150 [125-262]; 193.2 (102.9) | 0 [0-1]; 1.4 (3.0) | 0 [0-0]; 0.6 (2.0) |
|         2 | 247 [214-378]; 323.6 (176.1) | 352 [285-524]; 424.5 (203.8) | 135 [113-183]; 167.9 (103.2) | 0 [0-1]; 1.1 (3.5) | 0 [0-0]; 0.4 (2.5) |
|         4 | 236 [209-296]; 275.9 (112.1) | 298 [259-417]; 354.6 (155.6) | 125 [106-149]; 148.9 (84.2)  | 0 [0-0]; 0.4 (1.2) | 0 [0-0]; 0.0 (0.1) |
|         8 | 210 [188-235]; 229.4 (79.8)  | 259 [231-290]; 279.7 (102.9) | 106 [85-123]; 119.4 (61.3)   | 0 [0-0]; 0.1 (0.4) | 0 [0-0]; 0.0 (0.1) |

- Spearman: share of time follower+panic vs time until 90% out: rho = 0.55, p = 3.272e-30
- Spearman: share of time in panic vs casualties: rho = 0.62, p = 1.85e-39

## Experiment 2: forced cognitive strategies (slow whoop, no helpers)
50 runs. Runs that ended with people still inside: 13; runs where 90% never got out (t90 censored at 900 s): 11 (all panic: 10, arousal-based: 1).

| strategy      | t90                          | evac_time                    | casualties          | incapacitated       | left_inside            |
|:--------------|:-----------------------------|:-----------------------------|:--------------------|:--------------------|:-----------------------|
| all rational  | 252 [240-274]; 251.1 (30.0)  | 317 [308-335]; 321.0 (29.8)  | 0 [0-0]; 0.1 (0.3)  | 0 [0-0]; 0.0 (0.0)  | 0 [0-0]; 0.0 (0.0)     |
| all familiar  | 274 [263-282]; 273.4 (23.6)  | 363 [360-393]; 375.6 (43.7)  | 0 [0-0]; 0.1 (0.3)  | 0 [0-0]; 0.0 (0.0)  | 0 [0-0]; 0.0 (0.0)     |
| all follower  | 274 [256-295]; 272.3 (34.0)  | 344 [323-392]; 352.2 (55.4)  | 0 [0-0]; 0.1 (0.3)  | 0 [0-0]; 0.0 (0.0)  | 0 [0-0]; 0.0 (0.0)     |
| all panic     | 900 [900-900]; 900.0 (0.0)   | 900 [900-900]; 900.0 (0.0)   | 6 [1-12]; 6.7 (6.0) | 4 [1-9]; 7.9 (11.3) | 42 [40-48]; 42.9 (7.1) |
| arousal-based | 276 [262-396]; 363.8 (203.7) | 384 [346-809]; 533.9 (259.9) | 1 [0-7]; 3.9 (5.2)  | 0 [0-1]; 0.6 (1.1)  | 0 [0-1]; 0.6 (1.1)     |

### Time until 90% out (s): one-way ANOVA with the fire as block
|             |   df |      F |        p |   partial eta2 |
|:------------|-----:|-------:|---------:|---------------:|
| C(strategy) |    4 | 100.19 |   0      |          0.918 |
| C(fire)     |    9 |   1.79 |   0.1034 |          0.31  |
| Residual    |   36 | nan    | nan      |        nan     |

Kruskal-Wallis: H = 25.52, p = 3.954e-05

Tukey HSD:

```
         Multiple Comparison of Means - Tukey HSD, FWER=0.05         
=====================================================================
   group1        group2    meandiff p-adj    lower     upper   reject
---------------------------------------------------------------------
all familiar  all follower     -1.1    1.0 -120.4591  118.2591  False
all familiar     all panic    626.6    0.0  507.2409  745.9591   True
all familiar  all rational    -22.3 0.9837 -141.6591   97.0591  False
all familiar arousal-based     90.4 0.2167  -28.9591  209.7591  False
all follower     all panic    627.7    0.0  508.3409  747.0591   True
all follower  all rational    -21.2 0.9865 -140.5591   98.1591  False
all follower arousal-based     91.5 0.2066  -27.8591  210.8591  False
   all panic  all rational   -648.9    0.0 -768.2591 -529.5409   True
   all panic arousal-based   -536.2    0.0 -655.5591 -416.8409   True
all rational arousal-based    112.7 0.0725   -6.6591  232.0591  False
---------------------------------------------------------------------
```

### Total evacuation time (s): one-way ANOVA with the fire as block
|             |   df |      F |        p |   partial eta2 |
|:------------|-----:|-------:|---------:|---------------:|
| C(strategy) |    4 |  46.92 |   0      |          0.839 |
| C(fire)     |    9 |   1.98 |   0.0711 |          0.331 |
| Residual    |   36 | nan    | nan      |        nan     |

Kruskal-Wallis: H = 27.84, p = 1.343e-05

Tukey HSD:

```
        Multiple Comparison of Means - Tukey HSD, FWER=0.05        
===================================================================
   group1        group2    meandiff p-adj   lower    upper   reject
-------------------------------------------------------------------
all familiar  all follower    -23.4 0.9925 -177.398  130.598  False
all familiar     all panic    524.4    0.0  370.402  678.398   True
all familiar  all rational    -54.6 0.8506 -208.598   99.398  False
all familiar arousal-based    158.3 0.0412    4.302  312.298   True
all follower     all panic    547.8    0.0  393.802  701.798   True
all follower  all rational    -31.2  0.978 -185.198  122.798  False
all follower arousal-based    181.7 0.0134   27.702  335.698   True
   all panic  all rational   -579.0    0.0 -732.998 -425.002   True
   all panic arousal-based   -366.1    0.0 -520.098 -212.102   True
all rational arousal-based    212.9 0.0026   58.902  366.898   True
-------------------------------------------------------------------
```

### Casualties: one-way ANOVA with the fire as block
|             |   df |      F |        p |   partial eta2 |
|:------------|-----:|-------:|---------:|---------------:|
| C(strategy) |    4 |   8.31 |   0.0001 |          0.48  |
| C(fire)     |    9 |   1.78 |   0.1055 |          0.309 |
| Residual    |   36 | nan    | nan      |        nan     |

Kruskal-Wallis: H = 19.55, p = 0.0006129

Tukey HSD:

```
       Multiple Comparison of Means - Tukey HSD, FWER=0.05        
==================================================================
   group1        group2    meandiff p-adj   lower    upper  reject
------------------------------------------------------------------
all familiar  all follower      0.0    1.0  -4.5214  4.5214  False
all familiar     all panic      6.6 0.0013   2.0786 11.1214   True
all familiar  all rational      0.0    1.0  -4.5214  4.5214  False
all familiar arousal-based      3.8 0.1373  -0.7214  8.3214  False
all follower     all panic      6.6 0.0013   2.0786 11.1214   True
all follower  all rational      0.0    1.0  -4.5214  4.5214  False
all follower arousal-based      3.8 0.1373  -0.7214  8.3214  False
   all panic  all rational     -6.6 0.0013 -11.1214 -2.0786   True
   all panic arousal-based     -2.8 0.4092  -7.3214  1.7214  False
all rational arousal-based      3.8 0.1373  -0.7214  8.3214  False
------------------------------------------------------------------
```

## Sensitivity analysis (one parameter at a time; slow whoop, no helpers, 50% trained)

| variant                     |   t90 |   casualties |   share_panic |   t90 vs baseline p |   casualties vs baseline p |   share_panic vs baseline p |
|:----------------------------|------:|-------------:|--------------:|--------------------:|---------------------------:|----------------------------:|
| baseline                    | 282.4 |          1.4 |          0.08 |             nan     |                    nan     |                     nan     |
| companion_probability = 0   | 259.8 |          0.7 |          0.06 |               0.006 |                      0.375 |                       0.195 |
| companion_probability = 0.6 | 276.2 |          0.6 |          0.07 |               0.477 |                      0.156 |                       0.734 |
| evacuees = 300              | 300.8 |          5.1 |          0.11 |               0.131 |                      0.094 |                       0.557 |
| evacuees = 75               | 264.9 |          0.3 |          0.03 |               0.111 |                      0.156 |                       0.25  |
| panic_threshold = 0.65      | 277.3 |          1.6 |          0.1  |               0.865 |                      0.75  |                       0.375 |
| panic_threshold = 0.85      | 274.3 |          1   |          0.05 |               0.516 |                      0.5   |                       0.055 |
| vision_radius = 15          | 276.1 |          2.2 |          0.1  |               0.77  |                      0.5   |                       0.82  |
| vision_radius = 5           | 265.2 |          0   |          0.02 |               0.125 |                      0.031 |                       0.078 |
