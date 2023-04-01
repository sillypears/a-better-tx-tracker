$(function() {
  const cardContainer = document.getElementById("card-container");
  const cardCountElem = document.getElementById("card-count");
  const cardTotalElem = document.getElementById("card-total");
  const loader = document.getElementById("loader");
  const cardLimit = parseInt(cardTotalElem.textContent)

  const cardIncrease = 12;
  const pageCount = Math.ceil(cardLimit / cardIncrease);
  let currentPage = 1;

  var throttleTimer;
  const throttle = (callback, time) => {
    if (throttleTimer) return;
  
    throttleTimer = true;
  
    setTimeout(() => {
      callback();
      throttleTimer = false;
    }, time);
  };

  const getRandomColor = () => {
    const h = Math.floor(Math.random() * 360);
    return `hsl(${h}deg, 90%, 85%)`;
  };
  
  const createCard = (card, index) => {
    let temp = ""
    temp += `<div class="card ${(!card.received) ? "not-":""}arrived">`
    temp += `<div class="recieve-toggle" onClick="toggleReceived(${card.id})"><i class="fa fa-envelope" aria-hidden="true"></i> </div>`
    temp +=  `<a class="link size-card-img" href="/entry/${card.id}">`
    temp += `<img src="${(card.image) ? card.image : "/static/img/missing.png"}" class="card-img-top size-card-img">`
    temp += `</a>`
    temp += `<div class="card-title text-center">`
    temp +=     `${card.maker_name.display}`
    temp +=   `</div>`
    temp +=   `<div class="card-body text-center">`
    temp +=     `<div>`
    temp +=       `${card.colorway}/${card.sculpt_name}`
    temp +=     `</div>`
    if (card.clw_total > 0) {
       temp += `<div><i class="fa-solid fa-calculator"></i> <span id="clw_num">`
       temp += (card.clw_num > 0) ? card.clw_num : "" 
       temp += `</span> /<span id="clw_total"> ${card.clw_total}</span></div>`
    }
    temp +=   `</div>`
    temp +=   `<div class="card-footer"><div class="row">`
    temp +=     `<div class="col"><div class="text-start">${card.is_sold}</div></div>`
    temp +=     `<div class="col"><div class="text-end">${card.will_sell}</div></div>`
    temp +=   `</div></div>`
    temp += `</div>`

    let c = document.createElement('div')
    c.className = "col-10 col-md-5 col-lg-3 col-xl-2"
    c.innerHTML = temp
    cardContainer.appendChild(c);
    return index
  };
  
  const addCards = (pageIndex, cards) => {
    currentPage = pageIndex;
    cardCountElem.innerHTML = parseInt(cardCountElem.innerHTML) + cards.length
    cards.forEach((card, i) => {
      temp = createCard(card, i)
    })
  };
  
  const handleInfiniteScroll = () => {
    throttle(() => {
      const endOfPage =
        window.innerHeight + window.pageYOffset >= document.body.offsetHeight;
      if (endOfPage) {
        $.ajax({
          url: `/api/entries/${cardIncrease}/${(currentPage+1)*cardIncrease}`,
          method: "GET",
          success: function(data) {
            addCards(currentPage+1, data);
          }
        })
      }
      if (currentPage === pageCount) {
        removeInfiniteScroll();
      }
    }, 1000);
  };
  
  const removeInfiniteScroll = () => {
    window.removeEventListener("scroll", handleInfiniteScroll);
  };
  window.onload = new function () {
    let initialLoad = document.querySelector('html').offsetHeight
    // console.log(initialLoad, cardIncrease*Math.floor(( (initialLoad/320))))
    let increase = (currentPage, Math.floor(cardIncrease*( (initialLoad/320)/6)))
    $.ajax({
      url: `/api/entries/${cardIncrease*increase}/${(currentPage-1)*cardIncrease*increase}`,
      method: "GET",
      success: function(data) {
        addCards(currentPage, data);
        loader.remove();
      }
    })

  };
  
  window.addEventListener("scroll", handleInfiniteScroll);
  console.log('hi')
})

function toggleReceived(id) {
  console.log(id)
  $.ajax({
    url: `/api/toggleEntry`,
    method: "POST",
    data: `{"toggleId": ${id}}`,
    dataType: "json",
    contentType: "application/json",
    success: function(data) {
      console.log(`Flipped ${id} to ${data.status}`)
    }
  })
}