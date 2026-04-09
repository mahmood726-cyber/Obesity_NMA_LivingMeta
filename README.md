# Obesity Pharmacotherapy NMA — Living Meta-Analysis

**Network Meta-Analysis: Tirzepatide vs Semaglutide vs Orforglipron for >=5% Body Weight Loss**

A living systematic review and network meta-analysis comparing approved-dose obesity pharmacotherapy agents via a star network with placebo as common comparator.

## Network Structure

```
Tirzepatide 15mg ──── Placebo ──── Semaglutide 2.4mg
                         │
                  Orforglipron 36mg
```

All edges are direct (each drug vs placebo). No head-to-head RCTs yet completed between active agents (SURMOUNT-5 recruiting; ACHIEVE-3 used oral sema comparator only).

## Trials Included

| Trial | NCT | Drug | n (arm/placebo) | >=5% WL (drug) | >=5% WL (placebo) | Follow-up |
|-------|-----|------|-----------------|----------------|-------------------|-----------|
| SURMOUNT-1 | NCT04184622 | Tirzepatide 15mg | 630/643 | 91% | 35% | 72w |
| SURMOUNT-2 | NCT04657003 | Tirzepatide 15mg | 311/315 | 83% | 32% | 72w |
| STEP-1 | NCT03548935 | Semaglutide 2.4mg | 1306/655 | 86% | 32% | 68w |
| STEP-2 | NCT03552757 | Semaglutide 2.4mg | 404/403 | 69% | 29% | 68w |
| Orforglipron Ph2 | NCT05051579 | Orforglipron 36mg | 54/54 | ~77% | ~10% | 36w |

## Key NMA Caveats

- All indirect comparisons via placebo node (star network)
- Follow-up heterogeneity: 36w (orforglipron) vs 68-72w (others)
- Diabetes status is an effect modifier (non-T2DM vs T2DM subgroups)
- Orforglipron estimate based on Phase 2 only (n~54); ATTAIN-1 Phase 3 results pending
- SURMOUNT-5 (tirzepatide vs semaglutide 2.4mg head-to-head) is recruiting

## Dashboard

[View Live Dashboard](https://mahmood726-cyber.github.io/Obesity_NMA_LivingMeta/)

## Citation

Ahmad M. Obesity Pharmacotherapy Network Meta-Analysis: Tirzepatide vs Semaglutide vs Orforglipron. Living Meta-Analysis v14.0, RapidMeta Platform, 2026.
