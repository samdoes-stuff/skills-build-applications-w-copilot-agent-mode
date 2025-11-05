import React from 'react';

const Workouts = () => {
  const [data, setData] = React.useState([]);
  React.useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Fetching Workouts from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = Array.isArray(json) ? json : json.results || [];
        setData(results);
        console.log('Workouts data:', results);
      })
      .catch(err => console.error('Error fetching Workouts:', err));
  }, []);
  // Determine table columns from first item
  const columns = data.length > 0 ? Object.keys(data[0]) : [];
  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-body">
          <h2 className="card-title mb-4 display-6">Workouts</h2>
          {data.length > 0 ? (
            <div className="table-responsive">
              <table className="table table-striped table-bordered">
                <thead className="table-light">
                  <tr>
                    {columns.map(col => (
                      <th key={col}>{col.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {data.map((item, idx) => (
                    <tr key={item.id || idx}>
                      {columns.map(col => (
                        <td key={col}>{item[col]}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="alert alert-info">No workouts found.</div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Workouts;
