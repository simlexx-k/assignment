import { useEffect, useState } from 'react';
import axios from 'axios';
import Link from 'next/link';

export default function Dashboard() {
  const [assignments, setAssignments] = useState([]);

  useEffect(() => {
    const fetchAssignments = async () => {
      try {
        const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/assignments`);
        setAssignments(response.data);
        console.log("Assignments fetched successfully.");
      } catch (error) {
        console.error("Failed to fetch assignments.", error.response ? error.response.data : error);
      }
    };

    fetchAssignments();

    // WebSocket connection setup
    const wsScheme = window.location.protocol === "https:" ? "wss" : "ws";
    const ws = new WebSocket(`${wsScheme}://${window.location.host}/ws/assignments/`); // INPUT_REQUIRED {Ensure the WebSocket URL is correct for your deployment environment}

    ws.onopen = () => {
      console.log('WebSocket Connected');
    };

    ws.onmessage = (e) => {
      const data = JSON.parse(e.data);
      console.log('Message from server:', data.message);
      // Assuming the server sends updated assignments list
      if (data.assignments) {
        setAssignments(data.assignments);
        console.log("Assignments updated in real-time.");
      }
    };

    ws.onerror = (e) => {
      console.error('WebSocket error:', e.message);
    };

    ws.onclose = () => {
      console.log('WebSocket Disconnected');
    };

    return () => {
      ws.close();
    };
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <h2>Your Assignments</h2>
      <ul>
        {assignments.map((assignment) => (
          <li key={assignment.id}>{assignment.title}</li>
        ))}
      </ul>
      <Link href="/">Back to Home</Link>
    </div>
  );
}