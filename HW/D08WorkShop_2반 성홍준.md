D08HW_2반 성홍준

```python
@app.route('/dctionary/<string:word>')
def dictionary(word):
    word_dict = {'apple':'사과', 'banana':'바나나'}
    return render_template('dictionary.html', word = word, word_dict = word_dict)
```

