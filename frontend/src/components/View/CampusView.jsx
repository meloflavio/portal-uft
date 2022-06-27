/**
 * CampusView view component.
 * @module components/View/CampusView
 */

import React from 'react';
import PropTypes from 'prop-types';

/**
 * CampusView view component class.
 * @function CampusView
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */
const CampusView = (props) => {
  const { content } = props;

  return (
    <div id="page-document" className="ui container viewwrapper campus-view">
      <header>
        <h1 className="documentFirstHeading">{content.title}</h1>
      </header>
      <div className="ui card" style={{ width: '720px' }}>
        {content.image && (
          <div className="image">
            <img src={content.image.download} alt="foto campus" />
          </div>
        )}
        <div className="content">
          {content.title && (
            <div className="header">Campus: {content.city.title}</div>
          )}
          <div>
            {content.description && (
              <div className="description">{content.description}</div>
            )}
          </div>
          <div>{content.city && <div>Cidade: {content.city.title}</div>}</div>
        </div>
        <div className="extra content">
          <div>{content.email && <div>Email: {content.email}</div>}</div>
          <div>
            {content.extension && <div>Ramal: {content.extension}</div>}
          </div>
        </div>
      </div>
    </div>
  );
};

/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */
CampusView.propTypes = {
  content: PropTypes.shape({
    title: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    image: PropTypes.object,
    city: PropTypes.object,
    email: PropTypes.string.isRequired,
    extension: PropTypes.string.isRequired,
  }).isRequired,
};

export default CampusView;
