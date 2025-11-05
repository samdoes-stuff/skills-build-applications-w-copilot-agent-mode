import React from 'react';
import { formatHeader } from '../utils/formatHeader';

const Teams = () => {
  const [data, setData] = React.useState([]);
  React.useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
    console.log('Fetching Teams from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = Array.isArray(json) ? json : json.results || [];
        setData(results);
        console.log('Teams data:', results);
      })
      .catch(err => console.error('Error fetching Teams:', err));
  }, []);
  // Determine table columns from first item
  const columns = data.length > 0 ? Object.keys(data[0]) : [];
  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-body">
          <h2 className="card-title mb-4 display-6">Teams</h2>
          {data.length > 0 ? (
            <div className="table-responsive">
              <table className="table table-striped table-bordered">
                <thead className="table-light">
                  <tr>
                    {columns.map(col => (
                      <th key={col}>{formatHeader(col)}</th>
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
            <div className="alert alert-info">No teams found.</div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Teams;
