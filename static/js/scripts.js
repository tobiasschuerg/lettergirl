const searchInput = document.querySelector("#search-input");
const cardsContainer = document.querySelector("#card-container");

// Add event listener for the keyup event
searchInput.addEventListener("keyup", () => {
  const searchTerm = searchInput.value.toLowerCase().trim();

  // Loop through all the cards
  cardsContainer.querySelectorAll(".card-item").forEach((card) => {
    const name = card.dataset.name.toLowerCase();

    // If the card name contains the search term, show the card; otherwise, hide it
    if (name.includes(searchTerm)) {
      card.classList.remove("d-none");
    } else {
      card.classList.add("d-none");
    }
  });
});

// Add event listener for the input event
searchInput.addEventListener("input", () => {
  if (searchInput.value.trim() === "") {
    // If the search input is empty, show all the cards
    cardsContainer.querySelectorAll(".card-item").forEach((card) => {
      card.classList.remove("d-none");
    });
  }
});
