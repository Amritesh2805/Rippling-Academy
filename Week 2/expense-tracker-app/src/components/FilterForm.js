import React, { useState } from 'react';
import { uniqueId } from '../utils';
import TransactionHistory from './TransactionHistory';


function FilterForm({ onNewTransaction ,transactions ,handleDeleteTransaction }) {
    const [nameValue, setNameValue] = useState('');
   
    const [dateValue, setDateValue] = useState([]);
    const [billtypeValue, setBilltypeValue] = useState(null);
    const [categoryValue, setCategoryValue] = useState(null);
    const [filter_transactions, setFilter] = useState(transactions);
    console.log(filter_transactions);
    function filtering(evt) {
        // evt.preventDefault();
        let trans = transactions;
        trans = trans.filter(ele => {
            //if (nameValue === "")
                return true;
            //return ele.nameValue = nameValue;
        });
        console.log(transactions);
        console.log(trans);
        setFilter(trans);
        console.log(filter_transactions);
        // const data = { id: uniqueId(), name: nameValue, date: dateValue,
        //          billtype: billtypeValue,
        //         amount: parseInt(amountValue), category: categoryValue,
        //         type: type };
        // // onNewTransaction(data);
        // setNameValue('');
        // setAmountValue('');
        // setDateValue([]);
        // setBilltypeValue([]);
        // setCategoryValue([]);
    }

    return (
        <div>
            <form className='filter-form'>
                <label className='filter_lable'>
                    Name
                    <div>
                        <input type="text" value={nameValue}
                            onChange={(e) => setNameValue(e.target.value)} />
                    </div>
                </label>
                
                <label className='filter_lable'>
                    Date
                    <div>
                        <input type="date" value={dateValue}
                            onChange={(e) => setDateValue(e.target.value)} />
                    </div>
                </label>
                <label className='filter_lable'>
                    Bill Type
                    <div>
                        <select value={billtypeValue}
                            onChange={(e) => setBilltypeValue(e.target.value)}>
                                <option value="">--Bill type--</option>
                                <optgroup label="--Bill type--">
                                <option value="Cash">Cash</option>
                                <option value="Cheque">Cheque</option>
                                <option value="Card">Card</option>
                                <option value="UPI">UPI</option>
                                </optgroup>
                        </select>
                        
                    </div>
                </label>
                <label className='filter_lable'>
                    Category
                    <div>
                        <select value={categoryValue}
                            onChange={(e) => setCategoryValue(e.target.value)}>
                                <option value="">--Category--</option>
                                <optgroup label="--Category--">
                                <option value="Mortgages">Mortgages</option>
                                <option value="Groceries">Groceries</option>
                                <option value="Home_maintainence">Home maintainence</option>
                                <option value="Travel">Travel</option>
                                <option value="Cash_Withdrawals">ATM/Cash Withdrawals</option>
                                <option value="Entertainment">Entertainment</option>
                                <option value="Others">Others...</option>
                                </optgroup>
                        </select>
                        
                    </div>
                </label>
                </form>
                <div className='add_buttons'>
                    <button className='filter_btn' onClick={(e) => filtering('income', e)}>Filter</button>
                </div>
            {/* </form> */}
            <TransactionHistory transactions={filter_transactions}
                onDeleteTransaction={handleDeleteTransaction} />      
        </div>
    )
}

export default FilterForm;