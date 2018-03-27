package com.xuef.ssm.domain;

import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;

public class EmployeeExample {
    protected String orderByClause;

    protected boolean distinct;

    protected List<Criteria> oredCriteria;

    public EmployeeExample() {
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

        protected void addCriterionForJDBCDate(String condition, Date value, String property) {
            if (value == null) {
                throw new RuntimeException("Value for " + property + " cannot be null");
            }
            addCriterion(condition, new java.sql.Date(value.getTime()), property);
        }

        protected void addCriterionForJDBCDate(String condition, List<Date> values, String property) {
            if (values == null || values.size() == 0) {
                throw new RuntimeException("Value list for " + property + " cannot be null or empty");
            }
            List<java.sql.Date> dateList = new ArrayList<java.sql.Date>();
            Iterator<Date> iter = values.iterator();
            while (iter.hasNext()) {
                dateList.add(new java.sql.Date(iter.next().getTime()));
            }
            addCriterion(condition, dateList, property);
        }

        protected void addCriterionForJDBCDate(String condition, Date value1, Date value2, String property) {
            if (value1 == null || value2 == null) {
                throw new RuntimeException("Between values for " + property + " cannot be null");
            }
            addCriterion(condition, new java.sql.Date(value1.getTime()), new java.sql.Date(value2.getTime()), property);
        }

        public Criteria andENoIsNull() {
            addCriterion("e_no is null");
            return (Criteria) this;
        }

        public Criteria andENoIsNotNull() {
            addCriterion("e_no is not null");
            return (Criteria) this;
        }

        public Criteria andENoEqualTo(Integer value) {
            addCriterion("e_no =", value, "eNo");
            return (Criteria) this;
        }

        public Criteria andENoNotEqualTo(Integer value) {
            addCriterion("e_no <>", value, "eNo");
            return (Criteria) this;
        }

        public Criteria andENoGreaterThan(Integer value) {
            addCriterion("e_no >", value, "eNo");
            return (Criteria) this;
        }

        public Criteria andENoGreaterThanOrEqualTo(Integer value) {
            addCriterion("e_no >=", value, "eNo");
            return (Criteria) this;
        }

        public Criteria andENoLessThan(Integer value) {
            addCriterion("e_no <", value, "eNo");
            return (Criteria) this;
        }

        public Criteria andENoLessThanOrEqualTo(Integer value) {
            addCriterion("e_no <=", value, "eNo");
            return (Criteria) this;
        }

        public Criteria andENoIn(List<Integer> values) {
            addCriterion("e_no in", values, "eNo");
            return (Criteria) this;
        }

        public Criteria andENoNotIn(List<Integer> values) {
            addCriterion("e_no not in", values, "eNo");
            return (Criteria) this;
        }

        public Criteria andENoBetween(Integer value1, Integer value2) {
            addCriterion("e_no between", value1, value2, "eNo");
            return (Criteria) this;
        }

        public Criteria andENoNotBetween(Integer value1, Integer value2) {
            addCriterion("e_no not between", value1, value2, "eNo");
            return (Criteria) this;
        }

        public Criteria andENameIsNull() {
            addCriterion("e_name is null");
            return (Criteria) this;
        }

        public Criteria andENameIsNotNull() {
            addCriterion("e_name is not null");
            return (Criteria) this;
        }

        public Criteria andENameEqualTo(String value) {
            addCriterion("e_name =", value, "eName");
            return (Criteria) this;
        }

        public Criteria andENameNotEqualTo(String value) {
            addCriterion("e_name <>", value, "eName");
            return (Criteria) this;
        }

        public Criteria andENameGreaterThan(String value) {
            addCriterion("e_name >", value, "eName");
            return (Criteria) this;
        }

        public Criteria andENameGreaterThanOrEqualTo(String value) {
            addCriterion("e_name >=", value, "eName");
            return (Criteria) this;
        }

        public Criteria andENameLessThan(String value) {
            addCriterion("e_name <", value, "eName");
            return (Criteria) this;
        }

        public Criteria andENameLessThanOrEqualTo(String value) {
            addCriterion("e_name <=", value, "eName");
            return (Criteria) this;
        }

        public Criteria andENameLike(String value) {
            addCriterion("e_name like", value, "eName");
            return (Criteria) this;
        }

        public Criteria andENameNotLike(String value) {
            addCriterion("e_name not like", value, "eName");
            return (Criteria) this;
        }

        public Criteria andENameIn(List<String> values) {
            addCriterion("e_name in", values, "eName");
            return (Criteria) this;
        }

        public Criteria andENameNotIn(List<String> values) {
            addCriterion("e_name not in", values, "eName");
            return (Criteria) this;
        }

        public Criteria andENameBetween(String value1, String value2) {
            addCriterion("e_name between", value1, value2, "eName");
            return (Criteria) this;
        }

        public Criteria andENameNotBetween(String value1, String value2) {
            addCriterion("e_name not between", value1, value2, "eName");
            return (Criteria) this;
        }

        public Criteria andEGenderIsNull() {
            addCriterion("e_gender is null");
            return (Criteria) this;
        }

        public Criteria andEGenderIsNotNull() {
            addCriterion("e_gender is not null");
            return (Criteria) this;
        }

        public Criteria andEGenderEqualTo(String value) {
            addCriterion("e_gender =", value, "eGender");
            return (Criteria) this;
        }

        public Criteria andEGenderNotEqualTo(String value) {
            addCriterion("e_gender <>", value, "eGender");
            return (Criteria) this;
        }

        public Criteria andEGenderGreaterThan(String value) {
            addCriterion("e_gender >", value, "eGender");
            return (Criteria) this;
        }

        public Criteria andEGenderGreaterThanOrEqualTo(String value) {
            addCriterion("e_gender >=", value, "eGender");
            return (Criteria) this;
        }

        public Criteria andEGenderLessThan(String value) {
            addCriterion("e_gender <", value, "eGender");
            return (Criteria) this;
        }

        public Criteria andEGenderLessThanOrEqualTo(String value) {
            addCriterion("e_gender <=", value, "eGender");
            return (Criteria) this;
        }

        public Criteria andEGenderLike(String value) {
            addCriterion("e_gender like", value, "eGender");
            return (Criteria) this;
        }

        public Criteria andEGenderNotLike(String value) {
            addCriterion("e_gender not like", value, "eGender");
            return (Criteria) this;
        }

        public Criteria andEGenderIn(List<String> values) {
            addCriterion("e_gender in", values, "eGender");
            return (Criteria) this;
        }

        public Criteria andEGenderNotIn(List<String> values) {
            addCriterion("e_gender not in", values, "eGender");
            return (Criteria) this;
        }

        public Criteria andEGenderBetween(String value1, String value2) {
            addCriterion("e_gender between", value1, value2, "eGender");
            return (Criteria) this;
        }

        public Criteria andEGenderNotBetween(String value1, String value2) {
            addCriterion("e_gender not between", value1, value2, "eGender");
            return (Criteria) this;
        }

        public Criteria andDeptNoIsNull() {
            addCriterion("dept_no is null");
            return (Criteria) this;
        }

        public Criteria andDeptNoIsNotNull() {
            addCriterion("dept_no is not null");
            return (Criteria) this;
        }

        public Criteria andDeptNoEqualTo(Integer value) {
            addCriterion("dept_no =", value, "deptNo");
            return (Criteria) this;
        }

        public Criteria andDeptNoNotEqualTo(Integer value) {
            addCriterion("dept_no <>", value, "deptNo");
            return (Criteria) this;
        }

        public Criteria andDeptNoGreaterThan(Integer value) {
            addCriterion("dept_no >", value, "deptNo");
            return (Criteria) this;
        }

        public Criteria andDeptNoGreaterThanOrEqualTo(Integer value) {
            addCriterion("dept_no >=", value, "deptNo");
            return (Criteria) this;
        }

        public Criteria andDeptNoLessThan(Integer value) {
            addCriterion("dept_no <", value, "deptNo");
            return (Criteria) this;
        }

        public Criteria andDeptNoLessThanOrEqualTo(Integer value) {
            addCriterion("dept_no <=", value, "deptNo");
            return (Criteria) this;
        }

        public Criteria andDeptNoIn(List<Integer> values) {
            addCriterion("dept_no in", values, "deptNo");
            return (Criteria) this;
        }

        public Criteria andDeptNoNotIn(List<Integer> values) {
            addCriterion("dept_no not in", values, "deptNo");
            return (Criteria) this;
        }

        public Criteria andDeptNoBetween(Integer value1, Integer value2) {
            addCriterion("dept_no between", value1, value2, "deptNo");
            return (Criteria) this;
        }

        public Criteria andDeptNoNotBetween(Integer value1, Integer value2) {
            addCriterion("dept_no not between", value1, value2, "deptNo");
            return (Criteria) this;
        }

        public Criteria andEJobIsNull() {
            addCriterion("e_job is null");
            return (Criteria) this;
        }

        public Criteria andEJobIsNotNull() {
            addCriterion("e_job is not null");
            return (Criteria) this;
        }

        public Criteria andEJobEqualTo(String value) {
            addCriterion("e_job =", value, "eJob");
            return (Criteria) this;
        }

        public Criteria andEJobNotEqualTo(String value) {
            addCriterion("e_job <>", value, "eJob");
            return (Criteria) this;
        }

        public Criteria andEJobGreaterThan(String value) {
            addCriterion("e_job >", value, "eJob");
            return (Criteria) this;
        }

        public Criteria andEJobGreaterThanOrEqualTo(String value) {
            addCriterion("e_job >=", value, "eJob");
            return (Criteria) this;
        }

        public Criteria andEJobLessThan(String value) {
            addCriterion("e_job <", value, "eJob");
            return (Criteria) this;
        }

        public Criteria andEJobLessThanOrEqualTo(String value) {
            addCriterion("e_job <=", value, "eJob");
            return (Criteria) this;
        }

        public Criteria andEJobLike(String value) {
            addCriterion("e_job like", value, "eJob");
            return (Criteria) this;
        }

        public Criteria andEJobNotLike(String value) {
            addCriterion("e_job not like", value, "eJob");
            return (Criteria) this;
        }

        public Criteria andEJobIn(List<String> values) {
            addCriterion("e_job in", values, "eJob");
            return (Criteria) this;
        }

        public Criteria andEJobNotIn(List<String> values) {
            addCriterion("e_job not in", values, "eJob");
            return (Criteria) this;
        }

        public Criteria andEJobBetween(String value1, String value2) {
            addCriterion("e_job between", value1, value2, "eJob");
            return (Criteria) this;
        }

        public Criteria andEJobNotBetween(String value1, String value2) {
            addCriterion("e_job not between", value1, value2, "eJob");
            return (Criteria) this;
        }

        public Criteria andESalaryIsNull() {
            addCriterion("e_salary is null");
            return (Criteria) this;
        }

        public Criteria andESalaryIsNotNull() {
            addCriterion("e_salary is not null");
            return (Criteria) this;
        }

        public Criteria andESalaryEqualTo(Short value) {
            addCriterion("e_salary =", value, "eSalary");
            return (Criteria) this;
        }

        public Criteria andESalaryNotEqualTo(Short value) {
            addCriterion("e_salary <>", value, "eSalary");
            return (Criteria) this;
        }

        public Criteria andESalaryGreaterThan(Short value) {
            addCriterion("e_salary >", value, "eSalary");
            return (Criteria) this;
        }

        public Criteria andESalaryGreaterThanOrEqualTo(Short value) {
            addCriterion("e_salary >=", value, "eSalary");
            return (Criteria) this;
        }

        public Criteria andESalaryLessThan(Short value) {
            addCriterion("e_salary <", value, "eSalary");
            return (Criteria) this;
        }

        public Criteria andESalaryLessThanOrEqualTo(Short value) {
            addCriterion("e_salary <=", value, "eSalary");
            return (Criteria) this;
        }

        public Criteria andESalaryIn(List<Short> values) {
            addCriterion("e_salary in", values, "eSalary");
            return (Criteria) this;
        }

        public Criteria andESalaryNotIn(List<Short> values) {
            addCriterion("e_salary not in", values, "eSalary");
            return (Criteria) this;
        }

        public Criteria andESalaryBetween(Short value1, Short value2) {
            addCriterion("e_salary between", value1, value2, "eSalary");
            return (Criteria) this;
        }

        public Criteria andESalaryNotBetween(Short value1, Short value2) {
            addCriterion("e_salary not between", value1, value2, "eSalary");
            return (Criteria) this;
        }

        public Criteria andHiredateIsNull() {
            addCriterion("hireDate is null");
            return (Criteria) this;
        }

        public Criteria andHiredateIsNotNull() {
            addCriterion("hireDate is not null");
            return (Criteria) this;
        }

        public Criteria andHiredateEqualTo(Date value) {
            addCriterionForJDBCDate("hireDate =", value, "hiredate");
            return (Criteria) this;
        }

        public Criteria andHiredateNotEqualTo(Date value) {
            addCriterionForJDBCDate("hireDate <>", value, "hiredate");
            return (Criteria) this;
        }

        public Criteria andHiredateGreaterThan(Date value) {
            addCriterionForJDBCDate("hireDate >", value, "hiredate");
            return (Criteria) this;
        }

        public Criteria andHiredateGreaterThanOrEqualTo(Date value) {
            addCriterionForJDBCDate("hireDate >=", value, "hiredate");
            return (Criteria) this;
        }

        public Criteria andHiredateLessThan(Date value) {
            addCriterionForJDBCDate("hireDate <", value, "hiredate");
            return (Criteria) this;
        }

        public Criteria andHiredateLessThanOrEqualTo(Date value) {
            addCriterionForJDBCDate("hireDate <=", value, "hiredate");
            return (Criteria) this;
        }

        public Criteria andHiredateIn(List<Date> values) {
            addCriterionForJDBCDate("hireDate in", values, "hiredate");
            return (Criteria) this;
        }

        public Criteria andHiredateNotIn(List<Date> values) {
            addCriterionForJDBCDate("hireDate not in", values, "hiredate");
            return (Criteria) this;
        }

        public Criteria andHiredateBetween(Date value1, Date value2) {
            addCriterionForJDBCDate("hireDate between", value1, value2, "hiredate");
            return (Criteria) this;
        }

        public Criteria andHiredateNotBetween(Date value1, Date value2) {
            addCriterionForJDBCDate("hireDate not between", value1, value2, "hiredate");
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