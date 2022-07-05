import React from 'react'
import Products from './Products'

function Home() {
  return (
    <div className='Heroes'>
      <div className="card bg-dark text-white border-0 ">
  <img src="https://www.jackjones.com/dw/image/v2/ABBT_PRD/on/demandware.static/-/Library-Sites-bestseller-content-library/default/dw66843902/jackjones/store-assets/static/2021/w1/update1/smart-widget/jj-aboutus/bp1_aboutus-row2-box1.jpg?sw=660" className="card-img" alt="Background"
  height="770px"/>
  <div className="card-img-overlay d-flex flex-column justify-content-center">
    <div className="container">
    <h5 className="card-title display-3 fw-bolder mb-0">NEW SEASON ARRIVALS</h5>
    <p className="card-text lead fs-2">Check out our apparels!</p> 
    </div>
  </div>
 </div>
 <Products/>
</div>
  )
}

export default Home
