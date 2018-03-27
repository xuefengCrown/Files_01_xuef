package com.xuef.ssm.domain;

import java.util.ArrayList;
import java.util.List;

public class DepartmentExample {
    protected String orderByClause;

    protected boolean distinct;

    protected List<Criteria> oredCriteria;

    public DepartmentExample() {
        oredCriteria = new ArrayList<Criteria>();
    }

    public void setOrderByClause(String orderByClause) {
        this.orderByClause = orderByClause;
    }

    public String getOrderByClause() {
        return orderByClause;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }

    public boolean isDistinct() {
        return distinct;
    }

    public List<Criteria> getOredCriteria() {
        return oredCriteria;
    }

    public void or(Criteria criteria) {
        oredCriteria.add(criteria);
    }

    public Criteria or() {
        Criteria criteria = createCriteriaInternal();
        oredCriteria.add(criteria);
        return criteria;
    }

    public Criteria createCriteria() {
        Criteria criteria = createCriteriaInternal();
        if (oredCriteria.size() == 0) {
            oredCriteria.add(criteria);
        }
        return criteria;
    }

    protected Criteria createCriteriaInternal() {
        Criteria criteria = new Criteria();
        return criteria;
    }

    public void clear() {
        oredCriteria.clear();
        orderByClause = null;
        distinct = false;
    }

    protected abstract static class GeneratedCriteria {
        protected List<Criterion> criteria;

        protected GeneratedCriteria() {
            super();
            criteria = new ArrayList<Criterion>();
        }

        public boolean isValid() {
            return criteria.size() > 0;
        }

        public List<Criterion> getAllCriteria() {
            return criteria;
        }

        public List<Criterion> getCriteria() {
            return criteria;
        }

        protected void addCriterion(String condition) {
            if (condition == null) {
                throw new RuntimeException("Value for condition cannot be null");
            }
            criteria.add(new Criterion(condition));
        }

        protected void addCriterion(String condition, Object value, String property) {
            if (value == null) {
                throw new RuntimeException("Value for " + property + " cannot be null");
            }
            criteria.add(new Criterion(condition, value));
        }

        protected void addCriterion(String condition, Object value1, Object value2, String property) {
            if (value1 == null || value2 == null) {
                throw new RuntimeException("Between values for " + property + " cannot be null");
            }
            criteria.add(new Criterion(condition, value1, value2));
        }

        public Criteria andDNoIsNull() {
            addCriterion("d_no is null");
            return (Criteria) this;
        }

        public Criteria andDNoIsNotNull() {
            addCriterion("d_no is not null");
            return (Criteria) this;
        }

        public Criteria andDNoEqualTo(Integer value) {
            addCriterion("d_no =", value, "dNo");
            return (Criteria) this;
        }

        public Criteria andDNoNotEqualTo(Integer value) {
            addCriterion("d_no <>", value, "dNo");
            return (Criteria) this;
        }

        public Criteria andDNoGreaterThan(Integer value) {
            addCriterion("d_no >", value, "dNo");
            return (Criteria) this;
        }

        public Criteria andDNoGreaterThanOrEqualTo(Integer value) {
            addCriterion("d_no >=", value, "dNo");
            return (Criteria) this;
        }

        public Criteria andDNoLessThan(Integer value) {
            addCriterion("d_no <", value, "dNo");
            return (Criteria) this;
        }

        public Criteria andDNoLessThanOrEqualTo(Integer value) {
            addCriterion("d_no <=", value, "dNo");
            return (Criteria) this;
        }

        public Criteria andDNoIn(List<Integer> values) {
            addCriterion("d_no in", values, "dNo");
            return (Criteria) this;
        }

        public Criteria andDNoNotIn(List<Integer> values) {
            addCriterion("d_no not in", values, "dNo");
            return (Criteria) this;
        }

        public Criteria andDNoBetween(Integer value1, Integer value2) {
            addCriterion("d_no between", value1, value2, "dNo");
            return (Criteria) this;
        }

        public Criteria andDNoNotBetween(Integer value1, Integer value2) {
            addCriterion("d_no not between", value1, value2, "dNo");
            return (Criteria) this;
        }

        public Criteria andDNameIsNull() {
            addCriterion("d_name is null");
            return (Criteria) this;
        }

        public Criteria andDNameIsNotNull() {
            addCriterion("d_name is not null");
            return (Criteria) this;
        }

        public Criteria andDNameEqualTo(String value) {
            addCriterion("d_name =", value, "dName");
            return (Criteria) this;
        }

        public Criteria andDNameNotEqualTo(String value) {
            addCriterion("d_name <>", value, "dName");
            return (Criteria) this;
        }

        public Criteria andDNameGreaterThan(String value) {
            addCriterion("d_name >", value, "dName");
            return (Criteria) this;
        }

        public Criteria andDNameGreaterThanOrEqualTo(String value) {
            addCriterion("d_name >=", value, "dName");
            return (Criteria) this;
        }

        public Criteria andDNameLessThan(String value) {
            addCriterion("d_name <", value, "dName");
            return (Criteria) this;
        }

        public Criteria andDNameLessThanOrEqualTo(String value) {
            addCriterion("d_name <=", value, "dName");
            return (Criteria) this;
        }

        public Criteria andDNameLike(String value) {
            addCriterion("d_name like", value, "dName");
            return (Criteria) this;
        }

        public Criteria andDNameNotLike(String value) {
            addCriterion("d_name not like", value, "dName");
            return (Criteria) this;
        }

        public Criteria andDNameIn(List<String> values) {
            addCriterion("d_name in", values, "dName");
            return (Criteria) this;
        }

        public Criteria andDNameNotIn(List<String> values) {
            addCriterion("d_name not in", values, "dName");
            return (Criteria) this;
        }

        public Criteria andDNameBetween(String value1, String value2) {
            addCriterion("d_name between", value1, value2, "dName");
            return (Criteria) this;
        }

        public Criteria andDNameNotBetween(String value1, String value2) {
            addCriterion("d_name not between", value1, value2, "dName");
            return (Criteria) this;
        }

        public Criteria andDLocationIsNull() {
            addCriterion("d_location is null");
            return (Criteria) this;
        }

        public Criteria andDLocationIsNotNull() {
            addCriterion("d_location is not null");
            return (Criteria) this;
        }

        public Criteria andDLocationEqualTo(String value) {
            addCriterion("d_location =", value, "dLocation");
            return (Criteria) this;
        }

        public Criteria andDLocationNotEqualTo(String value) {
            addCriterion("d_location <>", value, "dLocation");
            return (Criteria) this;
        }

        public Criteria andDLocationGreaterThan(String value) {
            addCriterion("d_location >", value, "dLocation");
            return (Criteria) this;
        }

        public Criteria andDLocationGreaterThanOrEqualTo(String value) {
            addCriterion("d_location >=", value, "dLocation");
            return (Criteria) this;
        }

        public Criteria andDLocationLessThan(String value) {
            addCriterion("d_location <", value, "dLocation");
            return (Criteria) this;
        }

        public Criteria andDLocationLessThanOrEqualTo(String value) {
            addCriterion("d_location <=", value, "dLocation");
            return (Criteria) this;
        }

        public Criteria andDLocationLike(String value) {
            addCriterion("d_location like", value, "dLocation");
            return (Criteria) this;
        }

        public Criteria andDLocationNotLike(String value) {
            addCriterion("d_location not like", value, "dLocation");
            return (Criteria) this;
        }

        public Criteria andDLocationIn(List<String> values) {
            addCriterion("d_location in", values, "dLocation");
            return (Criteria) this;
        }

        public Criteria andDLocationNotIn(List<String> values) {
            addCriterion("d_location not in", values, "dLocation");
            return (Criteria) this;
        }

        public Criteria andDLocationBetween(String value1, String value2) {
            addCriterion("d_location between", value1, value2, "dLocation");
            return (Criteria) this;
        }

        public Criteria andDLocationNotBetween(String value1, String value2) {
            addCriterion("d_location not between", value1, value2, "dLocation");
            return (Criteria) this;
        }
    }

    public static class Criteria extends GeneratedCriteria {

        protected Criteria() {
            super();
        }
    }

    public static class Criterion {
        private String condition;

        private Object value;

        private Object secondValue;

        private boolean noValue;

        private boolean singleValue;

        private boolean betweenValue;

        private boolean listValue;

        private String typeHandler;

        public String getCondition() {
            return condition;
        }

        public Object getValue() {
            return value;
        }

        public Object getSecondValue() {
            return secondValue;
        }

        public boolean isNoValue() {
            return noValue;
        }

        public boolean isSingleValue() {
            return singleValue;
        }

        public boolean isBetweenValue() {
            return betweenValue;
        }

        public boolean isListValue() {
            return listValue;
        }

        public String getTypeHandler() {
            return typeHandler;
        }

        protected Criterion(String condition) {
            super();
            this.condition = condition;
            this.typeHandler = null;
            this.noValue = true;
        }

        protected Criterion(String condition, Object value, String typeHandler) {
            super();
            this.condition = condition;
            this.value = value;
            this.typeHandler = typeHandler;
            if (value instanceof List<?>) {
                this.listValue = true;
            } else {
                this.singleValue = true;
            }
        }

        protected Criterion(String condition, Object value) {
            this(condition, value, null);
        }

        protected Criterion(String condition, Object value, Object secondValue, String typeHandler) {
            super();
            this.condition = condition;
            this.value = value;
            this.secondValue = secondValue;
            this.typeHandler = typeHandler;
            this.betweenValue = true;
        }

        protected Criterion(String condition, Object value, Object secondValue) {
            this(condition, value, secondValue, null);
        }
    }
}