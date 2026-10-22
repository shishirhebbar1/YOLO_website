# Synthetic detection fixture EDA
Source: shishirhebbar1/YOLO_website at commit a036695f0951ba90fff505bcbdf991ac9ad6fa8b.

## Findings
{
  "records": 6,
  "columns": 9,
  "unique_image_ids": 6,
  "unique_classes": 6,
  "unique_model_groups": 3,
  "missing_cells": 0,
  "duplicate_rows": 0,
  "duplicate_image_ids": 0,
  "all_synthetic": true,
  "all_scores_and_coordinates_in_unit_interval": true,
  "all_dimensions_positive": true,
  "all_boxes_within_unit_image": true
}

Confidence mean: 0.743333; median: 0.865000; range: 0.25–0.95.
Normalized box area range: 4.00%–21.00%; mean: 9.0833%.

Model grouping summary:
               records  confidence_mean  confidence_median  confidence_min  confidence_max  mean_box_area_fraction
model_variant                                                                                                     
food                 2            0.765              0.765            0.62            0.91                  0.0425
hardhat              2            0.915              0.915            0.88            0.95                  0.1300
pascal               2            0.550              0.550            0.25            0.85                  0.1000

Illustrative confidence filtering (no records removed from main analysis):
 illustrative_threshold  retained_records  total_records
                   0.00                 6              6
                   0.25                 6              6
                   0.50                 5              6
                   0.75                 4              6
                   0.90                 2              6
                   0.95                 1              6

## Assumption and specification checks
- All six records retained; no exclusions, imputations or outlier removal.
- Synthetic status is true on all six rows; real-world representativeness is not testable from this fixture.
- Scores and normalized coordinates in [0,1], positive dimensions, box edges inside [0,1]: all checked and passed.
- Coordinate convention (x rightward, y downward) follows the fixture documentation and is used in plots; cannot be verified against source images because none are provided.
- Model names and classes are illustrative, not verified against model weights.
- Descriptive EDA only: no normality, equal variance, independence, or model-performance assumptions made. No statistical significance claims.
- Confidence thresholds are illustrative >= rules, not validated or optimized choices. The threshold table gives retention sensitivity.

## Caveats
Six hand-authored rows with one record per class are insufficient for performance estimation, calibration, distributional inference or meaningful model comparisons. Synthetic scores are not verified probabilities. Figures show unit canvases rather than real images. Group averages are fixture summaries only.

## Reproduce
python /mnt/workspace/1feb0846-954b-4afa-b414-cdf9621c265b/yolo_eda.py

Versions:
{
  "python": "3.12.14 | packaged by conda-forge | (main, Aug 21 2026, 22:36:41) [GCC 14.4.0]",
  "pandas": "2.2.3",
  "numpy": "1.26.4",
  "matplotlib": "3.9.2"
}
