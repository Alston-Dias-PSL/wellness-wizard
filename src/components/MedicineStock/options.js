export default {
    title: 'Line (discrete)',
    axes: {
      bottom: {
        title: 'Medicines',
        mapsTo: 'key',
        scaleType: 'labels',
      },
      left: {
        mapsTo: 'value',
        title: 'Stock sold',
        scaleType: 'linear',
      },
    },
    height: '400px',
  };
  