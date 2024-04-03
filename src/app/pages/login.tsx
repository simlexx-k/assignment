import React from 'react';
import { useRouter } from 'next/router';
import axios from 'axios';

const LoginPage = () => {
  const router = useRouter();

  const handleSubmit = async (event) => {
    event.preventDefault();
    const email = event.target.email.value;
    const password = event.target.password.value;

    try {
      const response = await axios.post('/api/login', { email, password });
      if (response.status === 200) {
        console.log('Login successful');
        router.push('/dashboard');
      } else {
        console.log('Login failed');
      }
    } catch (error) {
      console.error('Login error:', error.response.data.message);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label htmlFor="email">Email:</label>
        <input type="email" id="email" name="email" required />
        <label htmlFor="password">Password:</label>
        <input type="password" id="password" name="password" required />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default LoginPage;