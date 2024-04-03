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
    <form onSubmit={handleSubmit} className="bg-backgroundLight min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-4 text-textColor">Login</h1>
      <div className="mb-4">
        <label htmlFor="email" className="text-textColor">Email:</label>
        <input type="email" id="email" name="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required className="border-borderColor rounded px-2 py-1" />
      </div>
      <div className="mb-4">
        <label htmlFor="password" className="text-textColor">Password:</label>
        <input type="password" id="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required className="border-borderColor rounded px-2 py-1" />
      </div>
      <button type="submit" className="bg-primary text-white py-2 px-4 rounded hover:bg-secondary">Login</button>
    </form>
  );
}