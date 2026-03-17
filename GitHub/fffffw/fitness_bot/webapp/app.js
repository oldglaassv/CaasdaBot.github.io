const ctx = document.getElementById('chart');

new Chart(ctx, {

type: 'line',

data: {

labels: ['1','2','3','4','5'],

datasets: [{
label: 'Weight',
data: [80,79,78,77,76]
}]

}

});
