document.getElementById("orderForm").addEventListener("submit", function(event) {
  event.preventDefault();

  // Fake pickup time = 20 minutes from now - needing to come up with a system, thinking 1 minute per order item
  const pickupTime = new Date();
  pickupTime.setMinutes(pickupTime.getMinutes() + 20);

  document.getElementById("pickupTime").textContent = pickupTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  document.getElementById("orderForm").style.display = "none";
  document.getElementById("confirmation").style.display = "block";
});
