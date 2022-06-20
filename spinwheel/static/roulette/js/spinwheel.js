console.log("spinwheel.js");
let roundSlots = [];
let roundId = null;

// CSRF
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function getCurrentRound() {
  $.ajax({
    url: '/api/round/get_current_round',
    method: 'GET',
    dataType: 'json',
    success: (result) => {
      console.log(result);
      $("#round-number").text(`Round #${result.id}`);
      roundSlots = result.slots.slots;
      roundId = result.id;
    },
    error: (error) => {
      console.log(error);
    }
  });
}

// Spin button
$("#spin-btn").click(() => {
  const csrftoken = getCookie('csrftoken');
  $.ajax({
    url: '/api/round/make_spin/',
    method: 'POST',
    dataType: 'json',
    headers: {"X-CSRFToken": csrftoken},
    data: {round_id: roundId},
    success: (result) => {
      console.log(result);
      if (result.value == 11) {
        getCurrentRound();
        console.log("Round is over. Get new round.");
        $("#spin-value-text").text(`And your number is... ${result.value} JACKPOT!`);
      } else {
        $("#spin-value-text").text(`And your number is... ${result.value}`);
      }
    },
    error: (error) => {
      console.log(error);
    }
  });
})

getCurrentRound();