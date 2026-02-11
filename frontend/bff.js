const express = require("express");
const axios = require("axios");
const path = require("path");

const app = express();
app.use(express.json());

const FASTAPI_BASE = "http://127.0.0.1:8000";

/* ---------- API ROUTES ---------- */

app.get("/api/products", async (req, res) => {
  try {
    const r = await axios.get(`${FASTAPI_BASE}/products`);
    res.json(r.data);
  } catch {
    res.status(500).json({ error: "Failed to fetch products" });
  }
});

app.post("/api/product", async (req, res) => {
  try {
    const r = await axios.post(`${FASTAPI_BASE}/product`, req.body);
    res.json(r.data);
  } catch (e) {
    res.status(e.response?.status || 500).json(e.response?.data);
  }
});

app.put("/api/product/:id", async (req, res) => {
  try {
    const r = await axios.put(
      `${FASTAPI_BASE}/product/${req.params.id}`,
      req.body
    );
    res.json(r.data);
  } catch (e) {
    res.status(e.response?.status || 500).json(e.response?.data);
  }
});

app.delete("/api/product/:id", async (req, res) => {
  try {
    await axios.delete(`${FASTAPI_BASE}/product/${req.params.id}`);
    res.json({ message: "deleted" });
  } catch {
    res.status(500).json({ error: "Delete failed" });
  }
});

/* ---------- SERVE REACT ---------- */

app.use(express.static(path.join(__dirname, "build")));

/**
 * SPA fallback
 * MUST be middleware, NOT app.get("*")
 */
app.use((req, res) => {
  res.sendFile(path.join(__dirname, "build", "index.html"));
});

app.listen(3000, "0.0.0.0", () => {
  console.log("✅ App running on port 3000");
});
