window.startSandbox = function startSandbox(canvasId) {
  const canvas = document.getElementById(canvasId);
  const ctx = canvas.getContext("2d");

  function resize() {
    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;
  }

  const planets = [
    { r: 60, speed: 0.02, size: 3 },
    { r: 100, speed: 0.012, size: 5 },
    { r: 150, speed: 0.008, size: 6 },
    { r: 210, speed: 0.005, size: 4 },
  ];

  function draw(t) {
    resize();
    const w = canvas.width;
    const h = canvas.height;
    const cx = w / 2;
    const cy = h / 2;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, w, h);

    ctx.strokeStyle = "rgba(0,234,255,0.15)";
    planets.forEach((p) => {
      ctx.beginPath();
      ctx.arc(cx, cy, p.r, 0, Math.PI * 2);
      ctx.stroke();
    });

    ctx.strokeStyle = "#ffcc33";
    ctx.beginPath();
    ctx.arc(cx, cy, 16, 0, Math.PI * 2);
    ctx.stroke();

    planets.forEach((p, i) => {
      const angle = t * 0.001 * p.speed * 60 + i;
      const x = cx + Math.cos(angle) * p.r;
      const y = cy + Math.sin(angle) * p.r;

      ctx.fillStyle = i === 2 ? "#00eaff" : "#ffffff";
      ctx.beginPath();
      ctx.arc(x, y, p.size, 0, Math.PI * 2);
      ctx.fill();
    });

    requestAnimationFrame(draw);
  }

  requestAnimationFrame(draw);
};
