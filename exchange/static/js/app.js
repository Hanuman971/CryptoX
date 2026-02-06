const marketRows = document.querySelectorAll(".table-row:not(.header)");

async function refreshMarkets() {
  try {
    const response = await fetch("/api/markets/");
    if (!response.ok) {
      return;
    }
    const data = await response.json();
    data.markets.forEach((market, index) => {
      const row = marketRows[index];
      if (!row) return;
      const priceEl = row.querySelector("span:nth-child(2)");
      const changeEl = row.querySelector("span:nth-child(3)");
      const volumeEl = row.querySelector("span:nth-child(4)");

      priceEl.textContent = `$${market.price}`;
      changeEl.textContent = `${market.change}%`;
      changeEl.classList.toggle("positive", market.change >= 0);
      changeEl.classList.toggle("negative", market.change < 0);
      volumeEl.textContent = `${market.volume} ${market.base}`;
    });
  } catch (error) {
    console.warn("Unable to refresh markets", error);
  }
}

setInterval(refreshMarkets, 8000);
