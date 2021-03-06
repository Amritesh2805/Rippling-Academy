import React from 'react';

function TransactionHistory({ transactions, onDeleteTransaction }) {
    return (
        <div>
            <h2>Transaction History</h2>
            <p className='Transaction_list_heading'>Type Name Date Category Amount</p>
            <ul className='transactions'>
                {
                    transactions.map((data) => 
                        <li key={data.id}>
                            <div>{data.billtype}</div>
                            <div>{data.name}</div>
                            <div>{data.date}</div>
                            <div>{data.category}</div>
                            <div>
                                <span>₹ {data.amount}</span>
                                <button onClick={() => onDeleteTransaction(data.id)}>␡</button>
                            </div>
                            
                        </li>
                    )
                }
            </ul>
        </div>
    )
}

export default TransactionHistory;