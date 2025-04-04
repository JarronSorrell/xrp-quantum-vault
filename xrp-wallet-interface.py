import React, { useState, useEffect } from 'react';
import { BarChart, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, Bar, ResponsiveContainer } from 'recharts';
import { Shield, Zap, BarChart2, Clock, RefreshCw, Briefcase, Lock, CreditCard, ArrowUpRight, ChevronDown, ArrowDown, ArrowUp } from 'lucide-react';

const XRPWalletInterface = () => {
  const [balance, setBalance] = useState(151765892.00);
  const [xrpPrice, setXrpPrice] = useState(2.73);
  const [transactions, setTransactions] = useState([]);
  const [lastUpdate, setLastUpdate] = useState(new Date());
  const [incomePerSecond] = useState(172.84);
  const [selectedAsset, setSelectedAsset] = useState('all');
  const [showAssetDropdown, setShowAssetDropdown] = useState(false);
  
  const assets = [
    { id: 'xrp', name: 'XRP', balance: 27580431, price: 2.73, change: 4.2, color: '#25A9E0' },
    { id: 'sol', name: 'SOL', balance: 245672, price: 180.35, change: 5.7, color: '#9945FF' },
    { id: 'ada', name: 'ADA', balance: 15243890, price: 0.64, change: -1.2, color: '#0033AD' },
    { id: 'hbar', name: 'HBAR', balance: 42568932, price: 0.13, change: 2.5, color: '#00BEDE' },
    { id: 'xlm', name: 'XLM', balance: 32568792, price: 0.18, change: 3.1, color: '#141414' },
    { id: 'aapl', name: 'AAPL (Tokenized)', balance: 45290, price: 178.72, change: 0.9, color: '#A2AAAD' },
    { id: 'msft', name: 'MSFT (Tokenized)', balance: 32150, price: 415.56, change: 1.3, color: '#00A4EF' },
    { id: 'googl', name: 'GOOGL (Tokenized)', balance: 25800, price: 175.89, change: -0.2, color: '#4285F4' },
  ];

  const performanceData = [
    { name: 'Jan', value: 3.2 },
    { name: 'Feb', value: 4.5 },
    { name: 'Mar', value: 2.1 },
    { name: 'Apr', value: 5.8 },
    { name: 'May', value: 4.9 },
    { name: 'Jun', value: 7.2 },
    { name: 'Jul', value: 6.1 },
    { name: 'Aug', value: 8.5 },
    { name: 'Sep', value: 9.7 },
    { name: 'Oct', value: 11.2 },
    { name: 'Nov', value: 10.8 },
    { name: 'Dec', value: 12.4 },
  ];

  const assetAllocation = assets.map(asset => ({
    name: asset.name,
    value: (asset.balance * asset.price),
    color: asset.color
  }));

  // Add initial transactions
  useEffect(() => {
    const initialTransactions = [
      { 
        id: 1, 
        date: new Date(new Date().getTime() - 12 * 60000).toLocaleString(), 
        description: 'CryptoHopper Bot - XRP/USD Pair', 
        amount: 42589.75, 
        asset: 'XRP',
        type: 'credit' 
      },
      { 
        id: 2, 
        date: new Date(new Date().getTime() - 37 * 60000).toLocaleString(), 
        description: 'OpenAI Operator Strategy - AAPL Exit', 
        amount: 124732.50, 
        asset: 'AAPL',
        type: 'credit' 
      },
      { 
        id: 3, 
        date: new Date(new Date().getTime() - 125 * 60000).toLocaleString(), 
        description: 'AI Arbitrage - XRP/SOL Spread', 
        amount: 87500.00, 
        asset: 'SOL',
        type: 'credit' 
      },
      { 
        id: 4, 
        date: new Date(new Date().getTime() - 240 * 60000).toLocaleString(), 
        description: 'XRPL DEX Liquidity Mining', 
        amount: 235000.00, 
        asset: 'XRP',
        type: 'credit' 
      }
    ];
    setTransactions(initialTransactions);
  }, []);

  // Continuously increment balance for real-time effect
  useEffect(() => {
    const interval = setInterval(() => {
      // Update balance every 50ms (20 times per second)
      const increment = incomePerSecond / 20;
      setBalance(prevBalance => prevBalance + increment);
      
      // Update last update time
      setLastUpdate(new Date());
      
      // Slightly vary XRP price
      setXrpPrice(prev => {
        const change = (Math.random() - 0.48) * 0.01;
        return Math.max(prev + change, 0);
      });
    }, 50);
    
    // Add new transactions periodically
    const transactionInterval = setInterval(() => {
      const descriptions = [
        'CryptoHopper Bot - XRP/USD Pair',
        'Operator Strategy - SOL Position',
        'AI Arbitrage - HBAR/XRP Spread',
        'XRPL DEX Liquidity Mining',
        'Operator Strategy - MSFT Position',
        'CryptoHopper Bot - ADA Trend Follow',
        'Tokenized GOOGL Dividends',
        'XRP/XLM Arbitrage Profit',
        'XRPL Validator Rewards'
      ];
      
      const assetOptions = ['XRP', 'SOL', 'ADA', 'HBAR', 'XLM', 'AAPL', 'MSFT', 'GOOGL'];
      
      const randomIndex = Math.floor(Math.random() * descriptions.length);
      const randomAmount = Math.floor(Math.random() * 50000) + 10000;
      const randomAsset = assetOptions[Math.floor(Math.random() * assetOptions.length)];
      
      const newTransaction = {
        id: Date.now(),
        date: new Date().toLocaleString(),
        description: descriptions[randomIndex],
        amount: randomAmount,
        asset: randomAsset,
        type: 'credit'
      };
      
      setTransactions(prevTransactions => [
        newTransaction,
        ...prevTransactions.slice(0, 9) // Keep only the 10 most recent transactions
      ]);
    }, 15000); // New transaction every 15 seconds
    
    return () => {
      clearInterval(interval);
      clearInterval(transactionInterval);
    };
  }, [incomePerSecond]);

  // Format currency
  const formatCurrency = (amount) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    }).format(amount);
  };

  return (
    <div className="bg-gray-50 p-6 rounded-lg shadow-lg w-full max-w-6xl mx-auto">
      {/* Header */}
      <div className="flex justify-between items-center mb-6">
        <div className="flex items-center space-x-2">
          <Shield className="text-blue-600" size={28} />
          <div>
            <h1 className="text-2xl font-bold text-gray-800">XRP Quantum Vault</h1>
            <p className="text-xs text-gray-500">Managed by OpenAI Operator • Secured by Ledger Nano X</p>
          </div>
        </div>
        <div className="flex items-center text-gray-500 text-sm">
          <Clock size={16} className="mr-1" />
          <span>Last updated: {lastUpdate.toLocaleTimeString()}</span>
        </div>
      </div>
      
      {/* Main Grid Layout */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
        {/* Balance Card */}
        <div className="lg:col-span-2">
          <div className="bg-gradient-to-r from-blue-600 to-blue-800 rounded-xl p-6 text-white shadow-lg h-full">
            <div className="flex justify-between items-center">
              <div>
                <p className="text-blue-100 mb-1">Total Portfolio Value</p>
                <h2 className="text-3xl font-bold tracking-tight">
                  {formatCurrency(balance)}
                </h2>
                <div className="mt-2 flex items-center">
                  <Zap size={16} className="mr-1" />
                  <span className="text-blue-100 text-sm">AI-operated multi-asset strategy</span>
                </div>
              </div>
              <div className="flex flex-col items-end">
                <div className="flex items-center space-x-2 mb-2">
                  <div className="h-2 w-2 bg-green-400 rounded-full animate-pulse"></div>
                  <span className="text-green-200 text-sm">Active Trading</span>
                </div>
                <div className="text-right">
                  <p className="text-xs text-blue-200">XRP Price</p>
                  <p className="text-lg font-semibold">${xrpPrice.toFixed(4)}</p>
                </div>
              </div>
            </div>
            <div className="mt-6">
              <div className="h-1 w-full bg-blue-400 bg-opacity-30 rounded-full overflow-hidden">
                <div className="h-full bg-green-400 rounded-full w-3/4 animate-pulse"></div>
              </div>
            </div>
          </div>
        </div>
        
        {/* Portfolio Performance */}
        <div className="bg-white rounded-xl p-6 shadow-lg h-full">
          <div className="flex justify-between items-center mb-4">
            <h3 className="font-semibold text-gray-700">AI Performance</h3>
            <div className="text-green-600 font-medium text-sm flex items-center">
              <ArrowUp size={16} className="mr-1" />
              <span>+18.7% YTD</span>
            </div>
          </div>
          <div className="h-48">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={performanceData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
                <XAxis dataKey="name" tick={{fontSize: 10}} />
                <YAxis tickFormatter={(value) => `${value}%`} tick={{fontSize: 10}} />
                <Tooltip formatter={(value) => [`${value}%`, 'Return']} />
                <Line 
                  type="monotone" 
                  dataKey="value" 
                  stroke="#2563eb" 
                  strokeWidth={2} 
                  dot={{r: 0}}
                  activeDot={{r: 4}} 
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
      
      {/* Second Row */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
        {/* Asset Allocation */}
        <div className="bg-white rounded-xl p-6 shadow-lg">
          <h3 className="font-semibold text-gray-700 mb-4">Asset Allocation</h3>
          <div className="h-48">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={assetAllocation}>
                <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
                <XAxis dataKey="name" tick={{fontSize: 10}} />
                <YAxis tickFormatter={(value) => value >= 1000000 ? `$${(value/1000000).toFixed(1)}M` : `$${(value/1000).toFixed(0)}K`} tick={{fontSize: 10}} />
                <Tooltip formatter={(value) => [formatCurrency(value), 'Value']} />
                <Bar dataKey="value" fill={(entry) => entry.color} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
        
        {/* Top Holdings */}
        <div className="lg:col-span-2 bg-white rounded-xl p-6 shadow-lg">
          <h3 className="font-semibold text-gray-700 mb-4">Top Holdings</h3>
          <div className="space-y-4">
            {assets.slice(0, 5).map(asset => (
              <div key={asset.id} className="flex items-center justify-between py-2 border-b border-gray-100">
                <div className="flex items-center">
                  <div className="w-8 h-8 rounded-full flex items-center justify-center mr-3" style={{backgroundColor: `${asset.color}20`}}>
                    <div className="w-4 h-4 rounded-full" style={{backgroundColor: asset.color}}></div>
                  </div>
                  <div>
                    <p className="font-medium text-gray-800">{asset.name}</p>
                    <p className="text-xs text-gray-500">{asset.balance.toLocaleString()} units</p>
                  </div>
                </div>
                <div className="text-right">
                  <p className="font-medium">{formatCurrency(asset.balance * asset.price)}</p>
                  <p className={`text-xs ${asset.change > 0 ? 'text-green-600' : 'text-red-600'}`}>
                    {asset.change > 0 ? '↑' : '↓'} {Math.abs(asset.change)}%
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
      
      {/* Transaction History */}
      <div className="bg-white rounded-xl shadow-lg overflow-hidden">
        <div className="flex justify-between items-center p-6 border-b border-gray-100">
          <h3 className="font-semibold text-gray-700">AI Trading Activity</h3>
          <div className="relative">
            <button 
              className="flex items-center text-sm text-gray-600 bg-gray-100 px-3 py-1 rounded-md"
              onClick={() => setShowAssetDropdown(!showAssetDropdown)}
            >
              {selectedAsset === 'all' ? 'All Assets' : assets.find(a => a.id === selectedAsset)?.name}
              <ChevronDown size={14} className="ml-2" />
            </button>
            
            {showAssetDropdown && (
              <div className="absolute right-0 mt-1 w-40 bg-white rounded-md shadow-lg z-10">
                <ul className="py-1">
                  <li 
                    className="px-3 py-2 text-sm cursor-pointer hover:bg-gray-100"
                    onClick={() => {
                      setSelectedAsset('all');
                      setShowAssetDropdown(false);
                    }}
                  >
                    All Assets
                  </li>
                  {assets.map(asset => (
                    <li 
                      key={asset.id}
                      className="px-3 py-2 text-sm cursor-pointer hover:bg-gray-100"
                      onClick={() => {
                        setSelectedAsset(asset.id);
                        setShowAssetDropdown(false);
                      }}
                    >
                      {asset.name}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>
        
        <table className="min-w-full">
          <thead>
            <tr className="bg-gray-50 text-gray-600 text-left text-xs uppercase font-semibold">
              <th className="px-6 py-3">Date/Time</th>
              <th className="px-6 py-3">AI Strategy</th>
              <th className="px-6 py-3">Asset</th>
              <th className="px-6 py-3 text-right">Amount</th>
              <th className="px-6 py-3 text-right">Portfolio Value</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100">
            {transactions
              .filter(t => selectedAsset === 'all' || t.asset.toLowerCase().includes(selectedAsset))
              .map((transaction, index) => {
                // Calculate running balance for each row (most recent at top)
                const rowBalance = balance - transactions
                  .slice(0, index)
                  .reduce((sum, t) => sum + t.amount, 0);
                  
                return (
                  <tr key={transaction.id} className={index === 0 ? "bg-blue-50" : ""}>
                    <td className="px-6 py-4 text-sm text-gray-500">{transaction.date}</td>
                    <td className="px-6 py-4 text-sm text-gray-800">{transaction.description}</td>
                    <td className="px-6 py-4 text-sm">
                      <span className="px-2 py-1 rounded-md text-xs font-medium" 
                        style={{
                          backgroundColor: assets.find(a => a.name === transaction.asset)?.color + '20' || '#E5E7EB',
                          color: assets.find(a => a.name === transaction.asset)?.color || '#374151'
                        }}>
                        {transaction.asset}
                      </span>
                    </td>
                    <td className="px-6 py-4 text-sm text-right text-green-600 font-medium">
                      +{formatCurrency(transaction.amount)}
                    </td>
                    <td className="px-6 py-4 text-sm text-right text-gray-800 font-medium">
                      {formatCurrency(rowBalance)}
                    </td>
                  </tr>
                );
              })}
          </tbody>
        </table>
      </div>
      
      {/* Footer */}
      <div className="mt-6 flex justify-between items-center text-sm text-gray-500">
        <div className="flex items-center">
          <Lock size={14} className="mr-1" />
          <span>Secured by Ledger Nano X</span>
        </div>
        <div className="flex items-center">
          <RefreshCw size={14} className="mr-1 animate-spin" style={{ animationDuration: '3s' }} />
          <span>OpenAI Operator Processing Trades</span>
        </div>
      </div>
    </div>
  );
};

export default XRPWalletInterface;
