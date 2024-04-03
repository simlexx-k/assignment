import React from 'react';
import Link from 'next/link';

const cors = require("cors");
self.use(cors());

const Home = () => {
  return (
    <div>
      <h1>Welcome to the Assignment App</h1>
      <p>This is the home page.</p>
      <Link href="/login">
        <a>Login</a>
      </Link>
      <br />
      <Link href="/dashboard">
        <a>Dashboard</a>
      </Link>
    </div>
  );
};

export default Home;