import axios from 'axios';
import { useState } from 'react';
import { useRouter } from 'next/router';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/login`, { email, password });
      console.log('Login successful:', response.data); // Log success response
      router.push('/dashboard'); // Redirect to dashboard on successful login
    } catch (error) {
      console.error('Login error:', error.response ? error.response.data : error); // Log the entire error message and trace
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1>Login</h1>
      <div>
        <label htmlFor="email">Email:</label>
        <input type="email" id="email" name="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
      </div>
      <div>
        <label htmlFor="password">Password:</label>
        <input type="password" id="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
      </div>
      <button type="submit">Login</button>
    </form>
  );
}