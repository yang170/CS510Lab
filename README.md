## Collection

```bash
python retrieve.py --config config/tfidf.yaml
```

## Evaluation

```bash
cat tfidf_result.txt | sacrebleu --width 4 target.txt
```

## Results

|           | title only  | title + article |
| --------- | ----------- | --------------- |
| tfidf     | **0.3428** | 0.1442          |
| bm25okapi | 0.3278      | **0.183**      |
| bm25l     | 0.2227      | 0.0923          |
| bm25plus  | 0.3202      | 0.1398          |
| bert      | 0.2643      | 0.1559          |
