import React, { useState } from 'react';
import { uniqueId } from '../utils';
import DatePicker from 'react-datepicker';
// import Select from 'react-select';


function TransactionForm({ onNewTransaction }) {
    const [nameValue, setNameValue] = useState('');
    const [amountValue, setAmountValue] = useState('');
    const [dateValue, setDateValue] = useState([]);
     const [billtypeValue, setBilltypeValue] = useState(null);

    // const billData = [
    //     {value: 1,
    //     label: "Cash"},
    //     {value: 2,
    //         label: "Cheque"},
    //         {value: 3,
    //             label: "Card"},
    //             {value: 4,
    //                 label: "UPI"},

    // ];
    const addTransaction = (type, evt) => {
        evt.preventDefault();

        const data = { id: uniqueId(), name: nameValue, date: dateValue,
                 billtype: billtypeValue,
                amount: parseInt(amountValue), type: type };

        onNewTransaction(data);

        setNameValue('');
        setAmountValue('');
        setDateValue([]);
        setBilltypeValue([]);
    }

    return (
        <div>
            <h3>Add New Transactions -</h3>
            <form className='transaction-form'>
                <label>
                    Name
                    <div>
                        <input type="text" value={nameValue}
                            onChange={(e) => setNameValue(e.target.value)} />
                    </div>
                </label>
                <label>
                    Amount
                    <div>
                        <input type="number" value={amountValue}
                            onChange={(e) => setAmountValue(e.target.value)} />
                    </div>
                </label>
                
                <label>
                    Date
                    <div>
                        <input type="date" value={dateValue}
                            onChange={(e) => setDateValue(e.target.value)} />
                    </div>
                </label>
                <label>
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
                        {/* <Select
                        value={billtypeValue}
                        onChange={(e) => setBilltypeValue(e)}
                        options={billData}
                        /> */}
                        
                    </div>
                </label>
                <div>
                    <button className='income-btn' onClick={(e) => addTransaction('income', e)}>Add Budget</button>
                    <button className='expense-btn' onClick={(e) => addTransaction('expense', e)}>Add Expense</button>
                </div>
            </form>
        </div>
    )
}

export default TransactionForm;