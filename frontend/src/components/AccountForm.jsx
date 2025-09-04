import { useState } from "react";
import api from "../api";

function AccountForm({ onAccountCreated }) {
  const [introducerId, setIntroducerId] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const payload = {
        introducer: introducerId ? parseInt(introducerId) : null,
      };
      const response = await api.post("/api/accounts/create/", payload);
      setMessage(
        `✅ Account created! Account ID = ${response.data.account_id}, Beneficiary = ${response.data.beneficiary}`
      );
      onAccountCreated();
      setIntroducerId("");
    } catch (error) {
      console.error("Error:", error.response?.data || error.message);
      setMessage("❌ Error: " + JSON.stringify(error.response?.data));
    }
  };

  return (
    <div>
      <h2>Create Account</h2>
      <form onSubmit={handleSubmit}>
        <label>Introducer ID (optional):</label>
        <input
          type="number"
          value={introducerId}
          onChange={(e) => setIntroducerId(e.target.value)}
        />
        <button type="submit">Create Account</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default AccountForm;
