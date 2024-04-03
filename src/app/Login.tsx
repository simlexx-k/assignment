import React, { useState } from 'react';
import axios from 'axios';
import { useRouter } from 'next/router';

const Login = () => {
  const [admissionNumber, setAdmissionNumber] = useState('');
  const [error, setError] = useState('');
  const router = useRouter();

  const handleLogin = async () => {
    try {
      const response = await axios.post('/api/login', { admissionNumber });
      console.log('Login successful', response.data);
      router.push('/dashboard'); // Redirect to dashboard after successful login
    } catch (err) {
      console.error('Login error', err.response || err);
      setError('Failed to login. Please check your admission number.');
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <input
        type="text"
        value={admissionNumber}
        onChange={(e) => setAdmissionNumber(e.target.value)}
        placeholder="Enter your admission number" // INPUT_REQUIRED {Placeholder text might need to be localized or customized based on application requirements}
      />
      <button onClick={handleLogin}>Login</button>
      {error && <p>{error}</p>}
    </div>
  );
};

export default Login;