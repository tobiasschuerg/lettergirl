const searchInput = document.querySelector("#search-input");
const cardsContainer = document.querySelector("#card-container");
const noResults = document.querySelector("#no-results");

searchInput.addEventListener("input", () => {
  const searchTerm = searchInput.value.toLowerCase().trim();
  console.log("keyup: " + searchTerm);
  let count = 0;

  // Loop through all the cards
  const cards = cardsContainer.querySelectorAll(".card-item");
  cards.forEach((card) => {
    const name = card.dataset.name.toLowerCase();

    // If the card name contains the search term, show the card; otherwise, hide it
    if (name.includes(searchTerm)) {
      card.classList.remove("d-none");
      count++;
    } else {
      card.classList.add("d-none");
    }
  });

  // Show or hide the "no results" message based on the count
  if (count === 0) {
    noResults.style.display = "block";
  } else {
    noResults.style.display = "none";
  }
});
