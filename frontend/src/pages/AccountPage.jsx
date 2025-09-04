import { useEffect, useState } from "react";
import api from "../api";
import AccountForm from "../components/AccountForm";

function AccountPage() {
  const [accounts, setAccounts] = useState([]);

  const getAccounts = () => {
    api.get("/api/accounts/")
      .then((res) => setAccounts(res.data))
      .catch((err) => console.error(err));
  };

  useEffect(() => {
    getAccounts();
  }, []);

  return (
    <div>
      <AccountForm onAccountCreated={getAccounts} />
      <h2>Accounts List</h2>
      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>Account No</th>
            <th>Introducer</th>
            <th>Beneficiary</th>
          </tr>
        </thead>
        <tbody>
          {accounts.map((acc) => (
            <tr key={acc.account_id}>
              <td>{acc.account_id}</td>
              <td>{acc.introducer || "-"}</td>
              <td>{acc.beneficiary || "-"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default AccountPage;
