'use strict';

const { E } = require('../utils/errors');

const isString = (v) => typeof v === 'string';
const isNumber = (v) => typeof v === 'number' && !Number.isNaN(v);
const isEmail = (v) => isString(v) && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
const isNonEmpty = (v) => isString(v) && v.trim().length > 0;

/**
 * Esquema simple: { field: { required, type, min, max, pattern, oneOf } }
 * Devuelve objeto saneado o lanza AppError 422.
 */
function validate(payload, schema) {
  const errors = [];
  const out = {};
  for (const [field, rules] of Object.entries(schema)) {
    const value = payload ? payload[field] : undefined;
    if (value === undefined || value === null || value === '') {
      if (rules.required) errors.push({ field, message: 'campo requerido' });
      continue;
    }
    if (rules.type === 'string' && !isString(value)) {
      errors.push({ field, message: 'debe ser string' }); continue;
    }
    if (rules.type === 'number') {
      const n = typeof value === 'number' ? value : Number(value);
      if (!isNumber(n)) { errors.push({ field, message: 'debe ser número' }); continue; }
      if (rules.min !== undefined && n < rules.min) errors.push({ field, message: `mínimo ${rules.min}` });
      if (rules.max !== undefined && n > rules.max) errors.push({ field, message: `máximo ${rules.max}` });
      out[field] = n;
      continue;
    }
    if (rules.type === 'email' && !isEmail(value)) {
      errors.push({ field, message: 'email inválido' }); continue;
    }
    if (rules.type === 'boolean' && typeof value !== 'boolean') {
      errors.push({ field, message: 'debe ser boolean' }); continue;
    }
    if (rules.min !== undefined && isString(value) && value.length < rules.min) {
      errors.push({ field, message: `mínimo ${rules.min} caracteres` }); continue;
    }
    if (rules.max !== undefined && isString(value) && value.length > rules.max) {
      errors.push({ field, message: `máximo ${rules.max} caracteres` }); continue;
    }
    if (rules.pattern && isString(value) && !rules.pattern.test(value)) {
      errors.push({ field, message: 'formato inválido' }); continue;
    }
    if (rules.oneOf && !rules.oneOf.includes(value)) {
      errors.push({ field, message: `debe ser uno de: ${rules.oneOf.join(', ')}` });
      continue;
    }
    out[field] = isString(value) ? value.trim() : value;
  }
  if (errors.length) throw E.unprocessable('Datos inválidos', errors);
  return out;
}

module.exports = { validate, isEmail, isNonEmpty };