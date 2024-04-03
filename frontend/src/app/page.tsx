import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <h1>Welcome to Assignment</h1>
      <p>
        <Link href="/login">Login</Link> | <Link href="/dashboard">Dashboard</Link>
      </p>
    </div>
  );
}