fetch("http://127.0.0.1:5000/api/data")
  .then(res => res.json())
  .then(data => {

    document.getElementById("total").innerText = data.total_requests;
    document.getElementById("suspicious").innerText = data.suspicious_requests;
    document.getElementById("percent").innerText = data.attack_percentage + "%";

    const ctx = document.getElementById('chart');

    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: ['Normal', 'Suspicious'],
        datasets: [{
          data: [
            data.total_requests - data.suspicious_requests,
            data.suspicious_requests
          ]
        }]
      }
    });

  })
  .catch(err => console.log(err));