const BACKEND_URL = window.PARAKLETOS_CONFIG.API_BASE.replace(/\/$/, "");

const statusLine = document.getElementById("statusLine");
const healthReadout = document.getElementById("healthReadout");
const volumeGrid = document.getElementById("volumeGrid");
const viewerTitle = document.getElementById("viewerTitle");
const viewerContent = document.getElementById("viewerContent");

const homeView = document.getElementById("homeView");
const viewerView = document.getElementById("viewerView");
const sandboxView = document.getElementById("sandboxView");

document.getElementById("homeBtn").addEventListener("click", () => showView("home"));
document.getElementById("sandboxBtn").addEventListener("click", () => showView("sandbox"));

function showView(name) {
  homeView.classList.add("hidden");
  viewerView.classList.add("hidden");
  sandboxView.classList.add("hidden");

  if (name === "home") homeView.classList.remove("hidden");
  if (name === "viewer") viewerView.classList.remove("hidden");
  if (name === "sandbox") sandboxView.classList.remove("hidden");
}

async function loadHealth() {
  try {
    const res = await fetch(`${BACKEND_URL}/health`);
    if (!res.ok) throw new Error(`Health failed: ${res.status}`);
    const data = await res.json();

    statusLine.textContent = `Backend ${data.backend} • DB ${data.database}`;
    healthReadout.textContent = `Status: ${data.status} | Volumes: ${data.volume_count} | φ=${data.phi} | 432Hz=${data.resonance}`;
  } catch (err) {
    statusLine.textContent = "Backend offline";
    healthReadout.textContent = err.message;
  }
}

async function loadVolumes() {
  volumeGrid.innerHTML = "";
  try {
    const res = await fetch(`${BACKEND_URL}/volumes`);
    if (!res.ok) throw new Error(`Volume list failed: ${res.status}`);
    const data = await res.json();

    data.forEach((v) => {
      const btn = document.createElement("button");
      btn.textContent = v.volume_id;
      btn.title = v.title;
      btn.addEventListener("click", () => loadVolume(v.volume_id));
      volumeGrid.appendChild(btn);
    });
  } catch (err) {
    volumeGrid.innerHTML = `<p>${err.message}</p>`;
  }
}

async function loadVolume(volumeId) {
  try {
    const res = await fetch(`${BACKEND_URL}/volumes/${volumeId}`);
    if (!res.ok) throw new Error(`Volume fetch failed: ${res.status}`);
    const data = await res.json();

    viewerTitle.textContent = `Volume ${data.volume_id}: ${data.title}`;
    viewerContent.textContent = data.content;
    showView("viewer");
  } catch (err) {
    viewerTitle.textContent = "Error";
    viewerContent.textContent = err.message;
    showView("viewer");
  }
}

async function boot() {
  await loadHealth();
  await loadVolumes();
  if (window.startSandbox) window.startSandbox("sandboxCanvas");
}

boot();
