function generateRandomColor(alphat = 0.2) {
	let red = Math.floor(parseInt(Math.random() * 255));
	let green = Math.floor(parseInt(Math.random() * 255));
	let blue = Math.floor(parseInt(Math.random() * 255));

	return `rgb(${red},${green},${blue}, ${alphat})`;
}

function loadChart(chart, endpoint) {
	fetch(endpoint)
		.then((response) => {
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			return response.json();
		})
		.then((jsonResponse) => {
			const labels = jsonResponse.data.labels;
			const datasets = jsonResponse.data.datasets;

			let background = [],
				borderColor = [];

			chart.data.datasets = [];
			chart.data.labels = [];

			chart.data.labels = labels;

			for (let i = 0; i < labels.length; i++) {
				background.push(generateRandomColor());
				borderColor.push(generateRandomColor(0));
			}

			datasets.forEach((dataset) => {
				dataset.backgroundColor = background;
				dataset.borderColor = borderColor;

				chart.data.datasets.push(dataset);
			});

			chart.update();
		})
		.catch((error) => {
			console.error(
				'Failed to fetch chart data from ' +
					endpoint +
					'!',
				error,
			);
		});
}

function createChart(ctx, type, text) {
	return new Chart(ctx, {
		type: type,
		options: {
			responsive: true,
			scales: {
				y: {
					beginAtZero: true,
				},
			},
			plugins: {
				title: {
					display: true,
					text: text,
					padding: {
						top: 10,
					},
				},
			},
		},
	});
}
