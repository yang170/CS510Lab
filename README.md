## Collection

```bash
python retrieve.py --config config/tfidf.yaml
```

## Evaluation

```bash
cat tfidf_result.txt | sacrebleu --width 4 target.txt
```
