import { Link } from 'react-router-dom'

export default function Navbar() {
  return (
    <nav>
      <h1>Breadly</h1>
      <Link to="/">Home</Link>
      <Link to="/recipe">Recipe</Link>
    </nav>
  )
}