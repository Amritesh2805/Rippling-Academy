
import {React , useState , useEffect} from "react";
import axios from "axios";
import { NavLink } from "react-router-dom";
import { ReactDOM } from "react";
import PropagateLoader from "react-spinners/PropagateLoader";
import './Products.css';

const Products = () => {
    const [data , setData ] = useState([]);
    const [loading , setLoading] = useState(true);
    const [filters, setFilters ] = useState(data);

    useEffect(() => {
        axios.get("https://fakestoreapi.com/products")
        .then(res=>{
            setData(res.data)
            setLoading(false)
            setFilters(res.data)
        })
    }, [])


const Loading = () => 
{
    return(
      <div className = "animations">
      <PropagateLoader color={"#011c4a"} loading={loading} size={15} />
      </div>
    )
}

const filterProduct = (cat) => {
  const updatedList = data.filter((x)=>x.category === cat);
  setFilters(updatedList);
}

const filterProduct1 = (price1,price2) => {
  if(!price1 && price2)
  price1=0;
  else if(price1 && !price2)
  price2=2000;
  else if(!price1 && !price2)
  {
    price1=0;
    price2=2000;
  }
  const updatedList = data.filter((x)=>x.price >= price1 && x.price <= price2);
  setFilters(updatedList);
}

const ShowProducts = () =>
{
    const [minprice,setMinprice] = useState();
    const [maxprice,setMaxprice] = useState();

    const handleSubmit = (e) => {
      e.preventDefault();
      filterProduct1(minprice,maxprice);
    }

    return(
        <>
              <div className="buttons d-flex justify-content-center mb-5 pb-5">
                   <button className="btn btn-outline-dark me-2" onClick={()=>setFilters(data)}>All</button>
                  <button className="btn btn-outline-dark me-2" onClick={()=>filterProduct("men's clothing")}>Men's Clothing</button> 
                 <button className="btn btn-outline-dark me-2" onClick={()=>filterProduct("women's clothing")}>Women's Clothing</button> 
                 <button className="btn btn-outline-dark me-2" onClick={()=>filterProduct("jewelery")}>Jewellery</button> 
                 <button className="btn btn-outline-dark me-2" onClick={()=>filterProduct("electronics")}>Electronics</button> 
      
              </div>
              
              <div className="row">
               <div className="col-12">
                 <p className="display-7 text-margin">Filter by price</p>
               </div>
              </div>

              <div>
                <form className="row g-3 justify-content-margin mb-5 pb-5" onSubmit={handleSubmit}>
                <div className="col-auto">
                  <input type="text" className="form-control" placeholder="$ Min" value={minprice} 
                  onChange={(e)=>setMinprice(e.target.value)}/>
                </div>
                <div className="col-auto">
                  <input type="text" className="form-control" placeholder="$ Max" value={maxprice} 
                  onChange={(e)=>setMaxprice(e.target.value)}/>
                </div>
                <div className="col-auto">
                  <button type="submit" className="btn btn-outline-dark me-2" >Go</button>
                </div>
              </form>
             </div>
        {
           
            filters.map((val,index)=>
            {
                return(
                    <>
                    <div className="card_head col-xl-3 col-lg-4 col-md-4 col-sm-6 col-xs-6 mb-4" key={index}>
                        <div className="card h-100 text-center p-2" key={val.id}>
                        <img src={val.image} className="card-img-top" alt={val.title} height="250px" />
                        <div className="card-body">
                            <h6 className="card-title mb-0">{val.title.substring(0,20)}...</h6>
                            <p className="card-text lead fw-bold">${val.price}</p>
                            <NavLink to={`/products/${val.id}`} className="btn btn-outline-dark">Buy now</NavLink>
                        </div>
                        </div>
                    </div>
                    </>
                )
            })
        }
        </>
    )
}
    

 return(
    <div>
      <div className="container my-5">
        <div className="row">
          <div className="col-12 mb-5">
            <p className="display-5 text-center">Latest Products</p>
          </div>
        </div>
        <div className="row justify-content-center">
          {loading ? <Loading /> : <ShowProducts />}
        </div>
      </div>
    </div>
 )
};

export default Products;
