# Synthetic detection test data

`synthetic_detections.csv` contains six hand-authored, entirely synthetic detection records for exercising CSV loading, confidence filtering, and bounding-box handling. These are not model predictions, training data, or benchmark results. No corresponding image files are supplied.

## Schema

- `image_id`: placeholder identifier; does not refer to a real image.
- `model_variant`: illustrative model grouping (`hardhat`, `food`, or `pascal`); not a verified model configuration.
- `class_name`: illustrative class label; not verified against the repository's model class mappings.
- `confidence`: synthetic score in [0, 1].
- `x_center`, `y_center`, `width`, `height`: normalized bounding-box coordinates in [0, 1], with x increasing rightward and y increasing downward. All boxes fit within the unit image.
- `is_synthetic`: always `true`.

The CSV is a custom tabular fixture, not the native YOLO annotation text format. It is not automatically wired into the application. The low-confidence record supports testing filtering logic. No runtime dependencies, application files, or model weights are changed.
