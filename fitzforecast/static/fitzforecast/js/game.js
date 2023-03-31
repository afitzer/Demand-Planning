// Define the canvas and context variables
var canvas = document.getElementById('game-canvas');
var ctx = canvas.getContext('2d');

// Define the ball and paddle variables
var ball = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    radius: 10,
    dx: 2,
    dy: 2
};
var paddle = {
    x: canvas.width / 2 - 50,
    y: canvas.height - 20,
    width: 100,
    height: 10,
    dx: 0
};

// Define the game loop function
function gameLoop() {
    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw the ball
    ctx.beginPath();
    ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
    ctx.fill();

    // Draw the paddle
    ctx.fillRect(paddle.x, paddle.y, paddle.width, paddle.height);

    // Update the ball position
    ball.x += ball.dx;
    ball.y += ball.dy;

    // Check for collisions with the walls
    if (ball.x + ball.radius > canvas.width || ball.x - ball.radius < 0) {
        ball.dx = -ball.dx;
    }
    if (
       ball.y - ball.radius < 0) {
        ball.dy = -ball.dy;
        } else if (ball.y + ball.radius > canvas.height - paddle.height) {
            if (ball.x > paddle.x && ball.x < paddle.x + paddle.width) {
                ball.dy = -ball.dy;
            } else {
                alert('Game Over');
                document.location.reload();
                clearInterval(intervalId);
            }
        }

    // Update the paddle position
    paddle.x += paddle.dx;

    // Keep the paddle within the canvas bounds
    if (paddle.x < 0) {
        paddle.x = 0;
    } else if (paddle.x + paddle.width > canvas.width) {
        paddle.x = canvas.width - paddle.width;
    }
}

// Add keyboard event listeners to move the paddle
document.addEventListener('keydown', function (event) {
    if (event.code === 'ArrowLeft') {
        paddle.dx = -5;
    } else if (event.code === 'ArrowRight') {
        paddle.dx = 5;
    }
});
document.addEventListener('keyup', function (event) {
    if (event.code === 'ArrowLeft' || event.code === 'ArrowRight') {
        paddle.dx = 0;
    }
});

// Start the game loop
var intervalId = setInterval(gameLoop, 10);
