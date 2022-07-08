import React from 'react'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
// import { LinkContainer } from 'react-router-bootstrap';
import { Outlet, NavLink } from 'react-router-dom';

const Header = () => {
  return (
    <div>
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand>Notes</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            {/* <LinkContainer to='/'>
            <Nav.Link>Home</Nav.Link>
            </LinkContainer>
            <LinkContainer to='/notes'>
            <Nav.Link>Notes</Nav.Link>
            </LinkContainer>
            <LinkContainer to='/create'>
            <Nav.Link>Create</Nav.Link>
            </LinkContainer> */}
            <Nav.Link as={NavLink} to="/home">Home</Nav.Link>
            <Nav.Link as={NavLink} to="/notes">Notes</Nav.Link>
            <Nav.Link as={NavLink} to="/create">Create</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    </div>
  );
} 

export default Header
