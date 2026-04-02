window.PARAKLETOS_CONFIG = {
  API_BASE:
    localStorage.getItem("parakletosApiBase") ||
    (location.hostname === "localhost" || location.hostname === "127.0.0.1" || location.protocol === "file:"
      ? "http://localhost:8000"
      : "https://parakletos-api.onrender.com")
};
