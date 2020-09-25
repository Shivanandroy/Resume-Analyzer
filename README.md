### ResumeAnalyzer
`ResumeAnalyzer` is an easy, lightweight python package to rank resume based on your requirement in just one line of code.



<iframe
  src="https://carbon.now.sh/embed?bg=rgba(255%2C255%2C255%2C1)&t=seti&wt=none&l=python&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=false&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=4x&wm=false&code=%2523%2520!%2520pip%2520install%2520ResumeAnalyzer%250Aimport%2520ResumeAnalyzer%2520as%2520ra%250A%250Aanalyzer%2520%253D%2520ra.ResumeAnalyzer()%250A%250A%2523%2520define%2520the%2520ranking%2520criteria%2520that%2520suits%2520your%2520requirement%250A%2523%2520E.g.%2520rank%2520candidates%2520based%2520on%2520Deep%2520Learning%252C%2520Machine%2520Learning%2520and%2520Time%2520Series%2520skills%250Asearch_criteria%2520%253D%2520%257B%250A%2520%2520%2520%2520%250A%2520%2520%2520%2520%2522Deep%2520Learning%2522%253A%2520%250A%2520%2520%255B%2522neural%2520networks%2522%252C%2520%2522cnn%2522%252C%2520%2522rnn%2522%252C%2520%2522ann%2522%252C%2520%2522lstm%2522%252C%2520%2522bert%2522%252C%2520%2522transformers%2522%255D%252C%250A%2520%2520%250A%2520%2520%2520%2520%2522Machine%2520Learning%2522%253A%2520%250A%2520%2520%255B%2522regression%2522%252C%2520%2522classification%2522%252C%2520%2522clustering%2522%252C%2520%2522time%2520series%2522%252C%2520%2522summarization%2522%252C%2520%2522nlp%2522%255D%252C%250A%2520%2520%250A%2520%2520%2520%2520%2522Time%2520Series%2522%253A%2520%2520%250A%2520%2520%255B%2522arima%2522%252C%2522sarimax%2522%252C%2520%2522prophet%2522%252C%2520%2522holt%2520winters%2522%255D%250A%2520%2520%250A%257D%250A%250A%2523%2520render%2520in%2520jupyter%2520notebook%250Aanalyzer.render(path%253D%2522Resume%2520Folder%252F%2522%252C%2520metadata%253Dsearch_criteria%252C%2520mode%253D%2522notebook%2522)%250A%250A%2523%2520render%2520in%2520browser%250Aanalyzer.render(path%253D%2522Resume%2520Folder%252F%2522%252C%2520metadata%253Dsearch_criteria%252C%2520mode%253D%2522browser%2522)"
  style="width: 900px; height: 646px; border:0; transform: scale(1); overflow:hidden;"
  sandbox="allow-scripts allow-same-origin">
</iframe>

![Alt Text](demo.gif)
