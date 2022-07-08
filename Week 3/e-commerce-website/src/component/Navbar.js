import React from 'react';
import { NavLink } from 'react-router-dom';
import {useSelector} from "react-redux";

function Navbar() {
  const state = useSelector((state)=>state.handleCart)
  return (
    <div>
      <nav className="navbar navbar-expand-lg bg-light py-3 shadow-sm">
  <div className="container">
    <NavLink className="header-logo" to="/">
      <img width="140px" height="70px" src="https://d1k8hez1mxkuxw.cloudfront.net/users/3800558/seller/profile/avatar552368.png"/>
    </NavLink>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarSupportedContent">
      <ul className="navbar-nav mx-auto mb-2 mb-lg-0">
        <li className="nav-item">
          <NavLink className="nav-link active" aria-current="page" to="/">Home</NavLink>
        </li>
        <li className="nav-item">
          <NavLink className="nav-link" to="/products">Products</NavLink>
        </li>
        <li className="nav-item">
          <NavLink className="nav-link" to="/about">About</NavLink>
        </li>
        <li className="nav-item">
          <NavLink className="nav-link" to="/contact">Contact us...</NavLink>
        </li>
      </ul>
      <div className="buttons">
        <NavLink to="/cart" className="btn btn-outline-dark ms-2">
            <i className="fa fa-shopping-cart me-1" aria-hidden="true">  ({state.length})</i>
        </NavLink>
      </div>
    </div>
  </div>
</nav>
    </div>
  )
}

export default Navbar
