let currentQuestion = 1;
const totalQuestions = document.querySelectorAll('.question').length;

function showQuestion(questionNumber) {
  document.querySelector(`#question${currentQuestion}`).style.display = 'none';
  document.querySelector(`#question${questionNumber}`).style.display = 'block';
  currentQuestion = questionNumber;
  updateNavigationButtons();
  updateProgressBar();
}

function nextQuestion() {
  if (currentQuestion < totalQuestions) {
    showQuestion(currentQuestion + 1);
  }
}

function prevQuestion() {
  if (currentQuestion > 1) {
    showQuestion(currentQuestion - 1);
  }
}

function updateNavigationButtons() {
  document.getElementById('prev-btn').disabled = currentQuestion === 1;
  document.getElementById('next-btn').style.display = currentQuestion === totalQuestions ? 'none' : 'inline-block';
  document.getElementById('submit-btn').style.display = currentQuestion === totalQuestions ? 'inline-block' : 'none';
}

function updateProgressBar() {
  const progress = (currentQuestion - 1) / (totalQuestions - 1) * 100;
  document.getElementById('progress-bar').style.width = `${progress}%`;
}
