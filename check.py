<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Participant Names</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <!-- Custom CSS -->
    <style>
        .marquee {
            white-space: nowrap;
            overflow: hidden;
            box-sizing: border-box;
            animation: marquee 15s linear infinite;
        }

        @keyframes marquee {
            0% {
                transform: translateX(100%);
            }

            100% {
                transform: translateX(-100%);
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="mt-5 mb-4">Participant Names</h1>
        <div class="marquee">
            <!-- Participant names will be dynamically inserted here -->
            <span class="badge badge-primary badge-pill mr-2">Participant 1</span>
            <span class="badge badge-primary badge-pill mr-2">Participant 2</span>
            <span class="badge badge-primary badge-pill mr-2">Participant 3</span>
            <!-- Add more participants as needed -->
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>


.matrix-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
    gap: 5px;
}

.matrix-cell {
    background-color: #000;
    color: #00ff00; /* Change text color as needed */
    font-size: 16px;
    text-align: center;
    padding: 10px;
    animation: animateMatrix 0.5s infinite alternate;
}

@keyframes animateMatrix {
    0% {
        opacity: 0;
        transform: translateY(-20px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

const participantNames = ['Participant 1', 'Participant 2', 'Participant 3', /* Add more names as needed */];

const matrixContainer = document.getElementById('matrix-container');

participantNames.forEach(name => {
    const cell = document.createElement('div');
    cell.classList.add('matrix-cell');
    cell.textContent = name;
    matrixContainer.appendChild(cell);
});