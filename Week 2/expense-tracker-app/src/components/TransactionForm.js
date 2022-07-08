import React, { useState } from 'react';
import { uniqueId } from '../utils';


function TransactionForm({ onNewTransaction }) {
    const [nameValue, setNameValue] = useState('');
    const [amountValue, setAmountValue] = useState('');
    const [dateValue, setDateValue] = useState([]);
     const [billtypeValue, setBilltypeValue] = useState(null);
     const [categoryValue, setCategoryValue] = useState(null);

    const addTransaction = (type, evt) => {
        evt.preventDefault();

        const data = { id: uniqueId(), name: nameValue, date: dateValue,
                 billtype: billtypeValue,
                amount: parseInt(amountValue), category: categoryValue,
                type: type };

        onNewTransaction(data);

        setNameValue('');
        setAmountValue('');
        setDateValue([]);
        setBilltypeValue([]);
        setCategoryValue([]);
    }

    return (
        <div>
            <h3>Add New Transactions -</h3>
            <form className='transaction-form'>
                <label className='lable'>
                    Name
                    <div>
                        <input type="text" value={nameValue}
                            onChange={(e) => setNameValue(e.target.value)} />
                    </div>
                </label>
                <label className='lable'>
                    Amount
                    <div>
                        <input type="number" value={amountValue}
                            onChange={(e) => setAmountValue(e.target.value)} />
                    </div>
                </label>
                
                <label className='lable'>
                    Date
                    <div>
                        <input type="date" value={dateValue}
                            onChange={(e) => setDateValue(e.target.value)} />
                    </div>
                </label>
                <label className='lable'>
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
                <label className='lable'>
                    Category
                    <div>
                        <select value={categoryValue}
                            onChange={(e) => setCategoryValue(e.target.value)}>
                                <option value="">--Category--</option>
                                <optgroup label="--Credits--">
                                <option value="Salary">Salary</option>
                                <option value="Bonus">Bonus</option>
                                <option value="Others_c">Others...</option>
                                </optgroup>
                                <optgroup label="--Debits--">
                                <option value="Mortgages">Mortgages</option>
                                <option value="Groceries">Groceries</option>
                                <option value="Home_maintainence">Home maintainence</option>
                                <option value="Travel">Travel</option>
                                <option value="Cash_Withdrawals">ATM/Cash Withdrawals</option>
                                <option value="Entertainment">Entertainment</option>
                                <option value="Others_d">Others...</option>
                                </optgroup>
                        </select>
                        {/* <Select
                        value={billtypeValue}
                        onChange={(e) => setBilltypeValue(e)}
                        options={billData}
                        /> */}
                        
                    </div>
                </label>
                </form>
                <div className='add_buttons'>
                    <button className='income-btn' onClick={(e) => addTransaction('income', e)}>Add Budget</button>
                    <button className='expense-btn' onClick={(e) => addTransaction('expense', e)}>Add Expense</button>
                </div>
            {/* </form> */}
        </div>
    )
}

export default TransactionForm;