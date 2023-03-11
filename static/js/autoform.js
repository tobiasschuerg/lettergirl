// Select all form inputs
const formInputs = document.querySelectorAll('form input')

// Loop through form inputs and add event listener to store input values in local storage
formInputs.forEach((input) => {
  input.addEventListener('input', () => {
    localStorage.setItem(input.id, input.value)
  })
})

// Loop through form inputs and restore input values from local storage
formInputs.forEach((input) => {
  const storedValue = localStorage.getItem(input.id)
  if (storedValue) {
    input.value = storedValue
  }
})
