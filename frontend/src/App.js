import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [email, setEmail] = useState("");
  const [mensagem, setMensagem] = useState("");
  const [bateriasFuturas, setBateriasFuturas] = useState([]);
  const [bateriasPassadas, setBateriasPassadas] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setMensagem("");
    setBateriasFuturas([]);
    setBateriasPassadas([]);

    try {
      const response = await axios.get(`http://localhost:8000/?email=${email}`);
      console.log("Resposta do backend:", response.data);

      if (
        response.data &&
        typeof response.data.mensagem === "string" &&
        Array.isArray(response.data.baterias_futuras) &&
        Array.isArray(response.data.baterias_passadas)
      ) {
        setMensagem(response.data.mensagem);
        setBateriasFuturas(response.data.baterias_futuras);
        setBateriasPassadas(response.data.baterias_passadas);
      } else {
        throw new Error("Resposta inesperada do servidor.");
      }
    } catch (err) {
      console.error("Erro ao carregar as baterias:", err);
      setError("Erro ao carregar as baterias.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Consulta de Baterias</h1>
      <form onSubmit={handleSubmit}>
        <label>
          E-mail:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <button type="submit" disabled={loading}>
          {loading ? "Carregando..." : "Consultar"}
        </button>
      </form>

      {error && <p className="error">{error}</p>}

      {mensagem && (
        <div className="result">
          <p>{mensagem}</p>
          <div className="baterias">
            <h3>Baterias Futuras</h3>
            {bateriasFuturas.length === 0 ? (
              <p>Nenhuma bateria futura encontrada.</p>
            ) : (
              <ul>
                {bateriasFuturas.map((bateria, index) => (
                  <li key={index}>
                    {bateria.data} às {bateria.horario} - {bateria.qtde_pessoas} pessoas
                  </li>
                ))}
              </ul>
            )}
            <h3>Baterias Passadas</h3>
            {bateriasPassadas.length === 0 ? (
              <p>Nenhuma bateria passada encontrada.</p>
            ) : (
              <ul>
                {bateriasPassadas.map((bateria, index) => (
                  <li key={index}>
                    {bateria.data} às {bateria.horario} - {bateria.qtde_pessoas} pessoas
                  </li>
                ))}
              </ul>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
