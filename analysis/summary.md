# Results of the BehaviorSpace experiments

## Experiment 1: helpers x alarm type x proportion trained
360 runs (36 conditions x 10 fires). Runs that ended with people still inside: 19; t90 censored at 900 s: 7.

### Time until 90% out (s): three-way ANOVA with the fire as block (type II)
|                                |   df |      F |        p |   partial eta2 |
|:-------------------------------|-----:|-------:|---------:|---------------:|
| C(helpers)                     |    3 |  59.13 |   0      |          0.36  |
| C(alarm)                       |    2 | 286.42 |   0      |          0.645 |
| C(trained)                     |    2 |   1.54 |   0.2155 |          0.01  |
| C(fire)                        |    9 |   2.18 |   0.0232 |          0.059 |
| C(helpers):C(alarm)            |    6 |  26.2  |   0      |          0.333 |
| C(helpers):C(trained)          |    6 |   2.15 |   0.0478 |          0.039 |
| C(alarm):C(trained)            |    4 |   0.87 |   0.4831 |          0.011 |
| C(helpers):C(alarm):C(trained) |   12 |   1    |   0.444  |          0.037 |
| Residual                       |  315 | nan    | nan      |        nan     |

- Kruskal-Wallis t90 by helpers: H = 47.02, p = 3.449e-10
- Kruskal-Wallis t90 by alarm: H = 198.42, p = 8.205e-44
- Kruskal-Wallis t90 by trained: H = 0.78, p = 0.6778

### Total evacuation time (s): three-way ANOVA with the fire as block (type II)
|                                |   df |      F |        p |   partial eta2 |
|:-------------------------------|-----:|-------:|---------:|---------------:|
| C(helpers)                     |    3 |  96.8  |   0      |          0.48  |
| C(alarm)                       |    2 | 390.07 |   0      |          0.712 |
| C(trained)                     |    2 |   0.82 |   0.4422 |          0.005 |
| C(fire)                        |    9 |   1.54 |   0.1313 |          0.042 |
| C(helpers):C(alarm)            |    6 |  39    |   0      |          0.426 |
| C(helpers):C(trained)          |    6 |   0.72 |   0.6377 |          0.013 |
| C(alarm):C(trained)            |    4 |   0.98 |   0.4188 |          0.012 |
| C(helpers):C(alarm):C(trained) |   12 |   0.65 |   0.8007 |          0.024 |
| Residual                       |  315 | nan    | nan      |        nan     |

- Kruskal-Wallis evac_time by helpers: H = 58.93, p = 9.972e-13
- Kruskal-Wallis evac_time by alarm: H = 187.54, p = 1.889e-41
- Kruskal-Wallis evac_time by trained: H = 1.50, p = 0.472

### Mean reaction time (s): three-way ANOVA with the fire as block (type II)
|                                |   df |      F |        p |   partial eta2 |
|:-------------------------------|-----:|-------:|---------:|---------------:|
| C(helpers)                     |    3 |  18.33 |   0      |          0.149 |
| C(alarm)                       |    2 | 154.75 |   0      |          0.496 |
| C(trained)                     |    2 |   1.89 |   0.1533 |          0.012 |
| C(fire)                        |    9 |   1.51 |   0.1443 |          0.041 |
| C(helpers):C(alarm)            |    6 |   5.34 |   0      |          0.092 |
| C(helpers):C(trained)          |    6 |   0.42 |   0.8671 |          0.008 |
| C(alarm):C(trained)            |    4 |   1.69 |   0.1528 |          0.021 |
| C(helpers):C(alarm):C(trained) |   12 |   0.34 |   0.9809 |          0.013 |
| Residual                       |  315 | nan    | nan      |        nan     |

- Kruskal-Wallis reaction_time by helpers: H = 42.19, p = 3.665e-09
- Kruskal-Wallis reaction_time by alarm: H = 164.00, p = 2.439e-36
- Kruskal-Wallis reaction_time by trained: H = 0.19, p = 0.9086

### Casualties: three-way ANOVA with the fire as block (type II)
|                                |   df |      F |        p |   partial eta2 |
|:-------------------------------|-----:|-------:|---------:|---------------:|
| C(helpers)                     |    3 |  10.79 |   0      |          0.093 |
| C(alarm)                       |    2 |   9.25 |   0.0001 |          0.055 |
| C(trained)                     |    2 |  10.34 |   0      |          0.062 |
| C(fire)                        |    9 |   5.94 |   0      |          0.145 |
| C(helpers):C(alarm)            |    6 |   4.01 |   0.0007 |          0.071 |
| C(helpers):C(trained)          |    6 |   4.88 |   0.0001 |          0.085 |
| C(alarm):C(trained)            |    4 |   3.11 |   0.0158 |          0.038 |
| C(helpers):C(alarm):C(trained) |   12 |   1.58 |   0.0966 |          0.057 |
| Residual                       |  315 | nan    | nan      |        nan     |

- Kruskal-Wallis casualties by helpers: H = 14.74, p = 0.002052
- Kruskal-Wallis casualties by alarm: H = 5.93, p = 0.05155
- Kruskal-Wallis casualties by trained: H = 21.69, p = 1.948e-05

### Descriptives per factor: median [IQR]; mean (SD)
| alarm      | t90                          | evac_time                    | reaction_time                | casualties         |
|:-----------|:-----------------------------|:-----------------------------|:-----------------------------|:-------------------|
| none       | 402 [293-542]; 447.5 (188.5) | 486 [359-671]; 536.8 (207.4) | 215 [163-311]; 246.2 (120.7) | 0 [0-1]; 1.4 (3.9) |
| slow whoop | 234 [204-270]; 241.4 (73.1)  | 300 [257-347]; 310.7 (67.5)  | 127 [99-145]; 123.8 (28.4)   | 0 [0-0]; 0.7 (2.1) |
| voice      | 208 [184-232]; 206.9 (29.6)  | 256 [224-283]; 256.8 (46.3)  | 111 [91-127]; 109.0 (24.9)   | 0 [0-0]; 0.2 (0.7) |

|   trained | t90                          | evac_time                    | reaction_time                | casualties         |
|----------:|:-----------------------------|:-----------------------------|:-----------------------------|:-------------------|
|       0   | 244 [205-324]; 309.5 (178.9) | 311 [260-423]; 375.3 (180.5) | 134 [104-164]; 153.8 (85.6)  | 0 [0-1]; 1.4 (4.0) |
|       0.5 | 241 [214-309]; 291.8 (138.9) | 309 [260-419]; 367.2 (167.4) | 129 [107-170]; 156.0 (83.4)  | 0 [0-0]; 0.7 (1.9) |
|       1   | 236 [202-292]; 294.6 (156.1) | 296 [248-386]; 361.8 (183.1) | 134 [104-173]; 169.2 (114.1) | 0 [0-0]; 0.2 (0.7) |

|   helpers | t90                          | evac_time                    | reaction_time                | casualties         |
|----------:|:-----------------------------|:-----------------------------|:-----------------------------|:-------------------|
|         0 | 274 [228-526]; 390.2 (230.3) | 369 [293-658]; 480.3 (248.6) | 148 [127-258]; 194.9 (114.7) | 0 [0-1]; 1.9 (4.6) |
|         2 | 252 [220-375]; 305.6 (132.5) | 329 [275-470]; 381.4 (145.1) | 143 [114-201]; 168.7 (97.1)  | 0 [0-0]; 0.7 (1.9) |
|         4 | 238 [208-278]; 267.6 (104.3) | 294 [251-362]; 330.4 (120.0) | 130 [110-154]; 151.5 (85.8)  | 0 [0-0]; 0.3 (0.8) |
|         8 | 215 [188-245]; 231.1 (76.2)  | 262 [232-303]; 280.3 (80.8)  | 107 [85-137]; 123.6 (63.4)   | 0 [0-0]; 0.2 (0.7) |

- Spearman: share of time follower+panic vs time until 90% out: rho = 0.48, p = 2.004e-22
- Spearman: share of time in panic vs casualties: rho = 0.60, p = 6.142e-36

## Experiment 2: forced cognitive strategies (slow whoop, no helpers)
50 runs. Runs that ended with people still inside: 10; runs where 90% never got out (t90 censored at 900 s): 11 (all panic: 10, arousal-based: 1).

| strategy      | t90                          | evac_time                   | casualties             |
|:--------------|:-----------------------------|:----------------------------|:-----------------------|
| all rational  | 256 [241-268]; 251.6 (25.5)  | 324 [311-343]; 325.8 (36.2) | 0 [0-0]; 0.0 (0.0)     |
| all familiar  | 272 [258-294]; 271.1 (30.6)  | 362 [350-392]; 370.0 (49.5) | 0 [0-0]; 0.1 (0.3)     |
| all follower  | 277 [251-292]; 272.2 (31.9)  | 351 [324-361]; 348.1 (44.3) | 0 [0-0]; 0.0 (0.0)     |
| all panic     | 900 [900-900]; 900.0 (0.0)   | 900 [900-900]; 900.0 (0.0)  | 13 [5-18]; 13.9 (11.6) |
| arousal-based | 286 [257-292]; 336.6 (201.1) | 376 [322-455]; 390.3 (77.2) | 0 [0-3]; 3.1 (6.5)     |

### Time until 90% out (s): one-way ANOVA with the fire as block
|             |   df |      F |        p |   partial eta2 |
|:------------|-----:|-------:|---------:|---------------:|
| C(strategy) |    4 | 105.85 |   0      |          0.922 |
| C(fire)     |    9 |   1.9  |   0.0834 |          0.322 |
| Residual    |   36 | nan    | nan      |        nan     |

Kruskal-Wallis: H = 25.50, p = 3.982e-05

Tukey HSD:

```
         Multiple Comparison of Means - Tukey HSD, FWER=0.05         
=====================================================================
   group1        group2    meandiff p-adj    lower     upper   reject
---------------------------------------------------------------------
all familiar  all follower      1.1    1.0 -116.7996  118.9996  False
all familiar     all panic    628.9    0.0  511.0004  746.7996   True
all familiar  all rational    -19.5 0.9897 -137.3996   98.3996  False
all familiar arousal-based     65.5 0.5185  -52.3996  183.3996  False
all follower     all panic    627.8    0.0  509.9004  745.6996   True
all follower  all rational    -20.6 0.9873 -138.4996   97.2996  False
all follower arousal-based     64.4 0.5351  -53.4996  182.2996  False
   all panic  all rational   -648.4    0.0 -766.2996 -530.5004   True
   all panic arousal-based   -563.4    0.0 -681.2996 -445.5004   True
all rational arousal-based     85.0 0.2603  -32.8996  202.8996  False
---------------------------------------------------------------------
```

### Total evacuation time (s): one-way ANOVA with the fire as block
|             |   df |      F |        p |   partial eta2 |
|:------------|-----:|-------:|---------:|---------------:|
| C(strategy) |    4 | 423.93 |   0      |          0.979 |
| C(fire)     |    9 |   4.36 |   0.0007 |          0.522 |
| Residual    |   36 | nan    | nan      |        nan     |

Kruskal-Wallis: H = 27.67, p = 1.454e-05

Tukey HSD:

```
         Multiple Comparison of Means - Tukey HSD, FWER=0.05         
=====================================================================
   group1        group2    meandiff p-adj    lower     upper   reject
---------------------------------------------------------------------
all familiar  all follower    -21.9  0.848  -83.3222   39.5222  False
all familiar     all panic    530.0    0.0  468.5778  591.4222   True
all familiar  all rational    -44.2  0.262 -105.6222   17.2222  False
all familiar arousal-based     20.3 0.8801  -41.1222   81.7222  False
all follower     all panic    551.9    0.0  490.4778  613.3222   True
all follower  all rational    -22.3 0.8394  -83.7222   39.1222  False
all follower arousal-based     42.2 0.3057  -19.2222  103.6222  False
   all panic  all rational   -574.2    0.0 -635.6222 -512.7778   True
   all panic arousal-based   -509.7    0.0 -571.1222 -448.2778   True
all rational arousal-based     64.5 0.0353    3.0778  125.9222   True
---------------------------------------------------------------------
```

### Casualties: one-way ANOVA with the fire as block
|             |   df |      F |        p |   partial eta2 |
|:------------|-----:|-------:|---------:|---------------:|
| C(strategy) |    4 |  10.31 |   0      |          0.534 |
| C(fire)     |    9 |   1.03 |   0.4344 |          0.205 |
| Residual    |   36 | nan    | nan      |        nan     |

Kruskal-Wallis: H = 30.17, p = 4.529e-06

Tukey HSD:

```
       Multiple Comparison of Means - Tukey HSD, FWER=0.05        
==================================================================
   group1        group2    meandiff p-adj   lower    upper  reject
------------------------------------------------------------------
all familiar  all follower     -0.1    1.0  -7.6409  7.4409  False
all familiar     all panic     13.8    0.0   6.2591 21.3409   True
all familiar  all rational     -0.1    1.0  -7.6409  7.4409  False
all familiar arousal-based      3.0 0.7897  -4.5409 10.5409  False
all follower     all panic     13.9    0.0   6.3591 21.4409   True
all follower  all rational      0.0    1.0  -7.5409  7.5409  False
all follower arousal-based      3.1 0.7692  -4.4409 10.6409  False
   all panic  all rational    -13.9    0.0 -21.4409 -6.3591   True
   all panic arousal-based    -10.8 0.0017 -18.3409 -3.2591   True
all rational arousal-based      3.1 0.7692  -4.4409 10.6409  False
------------------------------------------------------------------
```

## Sensitivity analysis (one parameter at a time; slow whoop, no helpers, 50% trained)

| variant                     |   t90 |   casualties |   share_panic |   t90 vs baseline p |   casualties vs baseline p |   share_panic vs baseline p |
|:----------------------------|------:|-------------:|--------------:|--------------------:|---------------------------:|----------------------------:|
| baseline                    | 273.6 |          0.9 |          0.07 |             nan     |                    nan     |                     nan     |
| companion_probability = 0   | 274.6 |          1.1 |          0.07 |               0.867 |                      0.5   |                       0.461 |
| companion_probability = 0.6 | 274.1 |          1.7 |          0.06 |               0.752 |                      0.656 |                       0.846 |
| evacuees = 300              | 301   |          3.8 |          0.07 |               0.037 |                      0.094 |                       0.426 |
| evacuees = 75               | 276.7 |          0.6 |          0.08 |               0.625 |                      0.25  |                       1     |
| panic_threshold = 0.65      | 269.6 |          1.3 |          0.06 |               0.389 |                      0.344 |                       0.496 |
| panic_threshold = 0.85      | 269.9 |          1.5 |          0.04 |               0.221 |                      0.75  |                       0.57  |
| vision_radius = 15          | 286.2 |          2.3 |          0.1  |               0.061 |                      0.062 |                       0.02  |
| vision_radius = 5           | 271   |          0.8 |          0.02 |               0.678 |                      0.75  |                       0.008 |
