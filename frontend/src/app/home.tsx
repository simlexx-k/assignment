
import Link from 'next/link';

const Home = () => {
  return (
    <div className="bg-backgroundLight min-h-screen text-textColor">
      <h1 className="text-3xl font-bold p-5">Welcome to the Assignment App</h1>
      <p className="p-5">This is the home page.</p>
      <div className="flex gap-4 p-5">
        <Link href="/login">
          <a className="bg-primary text-white py-2 px-4 rounded hover:bg-secondary">Login</a>
        </Link>
        <Link href="/dashboard">
          <a className="bg-primary text-white py-2 px-4 rounded hover:bg-secondary">Dashboard</a>
        </Link>
      </div>
    </div>
  );
};

export default Home;