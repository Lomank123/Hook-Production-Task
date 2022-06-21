let roundId = null;
const activeUsersTable = $("#active-users-table");
const userCountTable = $("#user-count-table");

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
    url: '/api/spinwheel/get_current_round',
    method: 'GET',
    dataType: 'json',
    success: (result) => {
      console.log(result);
      $("#round-number").text(`Round #${result.id}`);
      roundId = result.id;
    },
    error: (error) => {
      console.log(error);
    }
  });
}

function getStats() {
  $.ajax({
    url: '/api/spinwheel/get_stats',
    method: 'get',
    dataType: 'json',
    success: (result) => {
      console.log(result);
      updateStats(result);
    },
    error: (error) => {
      console.log(error);
    }
  });
}

  // Clear old stats
function clearStats() {
  activeUsersTable.empty();
  userCountTable.empty();

  const c1 = $(`
    <tr>
      <th>User id</th>
      <th>Round count</th>
      <th>Average spins per round</th>
    </tr>
  `)

  const c2 = $(`
    <tr>
      <th>Round id</th>
      <th>User count</th>
    </tr>
  `)

  activeUsersTable.append(c1);
  userCountTable.append(c2);
}

function updateStats(data) {
  clearStats();
  data.active_users.forEach(element => {
    let rows = $(`
      <tr>
        <td scope='row'>${element.user_id}</td>
        <td scope='row'>${element.round_count}</td>
        <td scope='row'>${element.avg_spins_count}</td>
      </tr>
    `)
    activeUsersTable.append(rows);
  });

  data.user_count_per_round.forEach(element => {
    let rows1 = $(`
      <tr>
        <td scope='row'>${element.spin_round_id}</td>
        <td scope='row'>${element.user_count}</td>
      </tr>
    `)
    userCountTable.append(rows1);
  });
}

// Spin button
$("#spin-btn").click(() => {
  const csrftoken = getCookie('csrftoken');
  $.ajax({
    url: '/api/spinwheel/make_spin/',
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
      getStats();
    },
    error: (error) => {
      console.log(error);
    }
  });
})

$("#stats-btn").click(() => {
  getStats();
})


getCurrentRound();
getStats();